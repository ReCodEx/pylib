from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .base import BaseEntity
from .submission import Submission
from .user import User
from pathlib import Path


class Solution(BaseEntity):
    '''
    Wrapper for assignment's solution data structure with additional features.
    '''

    def __init__(self, data: dict):
        super().__init__(data)
        self._last_submission = self.get("lastSubmission")
        if self._last_submission:
            self._last_submission = Cache.cache().inject(Submission, Submission(self._last_submission))

    def update(self, data: dict):
        '''
        Updates the solution with new data (e.g., after setting a flag or bonus points).
        '''
        super().update(data)
        self._last_submission = self.get("lastSubmission")
        if self._last_submission:
            self._last_submission = Cache.cache().inject(Submission, Submission(self._last_submission))

    def refresh(self):
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_solution,
            path_params={"id": self.id()}).get_payload()
        self.update(data)

    def get_author(self):
        '''
        Gets the author of the solution.
        '''
        author_id = self._data.get("authorId")
        return Cache.cache().get(User, author_id) if author_id else None

    def get_last_submission(self) -> Submission | None:
        '''
        Gets the last submission of the solution, or None if there is no submission.
        The last submission is the one that counts for grading.
        '''
        return self._last_submission

    def download(self, path: str):
        '''
        Downloads the solution in a .zip archive to the specified path.
        The path should be either a file name path or a directory path.
        In the latter case, the file will be named {solution_id}.zip.
        '''
        if Path(path).is_dir():
            path = Path(path) / f"{self.id()}.zip"
        elif not Path(path).parent.exists():
            raise Exception(f"Directory {Path(path).parent} does not exist")

        client = Cache.cache().get_client()
        client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_download_solution_archive,
            path_params={"id": self.id()}
        ).save_to_file(path)

    def set_flag(self, flag: str, value: bool):
        '''
        Sets the flag of the solution to the specified value.
        '''
        if flag not in ["accepted", "reviewRequested"]:
            raise Exception(f"Invalid flag: {flag}")
        client = Cache.cache().get_client()
        payload = client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_set_flag,
            path_params={"id": self.id(), "flag": flag},
            body={"value": value}
        ).get_payload()
        if "solutions" in payload:
            solutions = [Solution(data) for data in payload["solutions"]]
            Cache.cache().inject(Solution, solutions)  # update solutions in the cache

    def set_bonus_points(self, bonus_points: int):
        '''
        Updates the bonus points of the assignment solution (bonus points may be negative).
        '''
        client = Cache.cache().get_client()
        payload = client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_set_bonus_points,
            path_params={"id": self.id()},
            body={"bonusPoints": bonus_points}
        ).get_payload()
        solutions = [Solution(data) for data in payload]
        Cache.cache().inject(Solution, solutions)  # update solutions in the cache

    def override_points(self, points: int | None):
        '''
        Overrides the points of the assignment solution (points may be negative).
        If points is None, the override is removed (ReCodEx-assigned points are used).
        '''
        client = Cache.cache().get_client()
        bonus_points = self.get("bonusPoints", 0)  # we need to keep them
        payload = client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_set_bonus_points,
            path_params={"id": self.id()},
            body={"bonusPoints": bonus_points, "overriddenPoints": points}
        ).get_payload()
        solutions = [Solution(data) for data in payload]
        Cache.cache().inject(Solution, solutions)  # update solutions in the cache

    def resubmit(self, debug: bool = False):
        '''
        Resubmits the solution for re-evaluation.
        Debug mode indicates whether more data are preserved in the results archive.
        '''
        client = Cache.cache().get_client()
        payload = client.send_request_by_callback(
            DefaultApi.submit_presenter_action_resubmit,
            path_params={"id": self.id()},
            body={"debug": debug}
        ).get_payload()
        if "solution" in payload:
            self.update(payload["solution"])
