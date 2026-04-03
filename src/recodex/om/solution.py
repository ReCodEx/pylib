from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .comments import CommentThread
from .base import BaseEntity
from .solution_review import SolutionReview
from .submission import Submission
from .user import User
from pathlib import Path


class SolutionFile(BaseEntity):
    '''
    Wrapper for solution file data structure (file metadata).
    This structure has no refresh (loading) method, it needs to be loaded from Solution.
    The automated zip exploration is not supported yet.
    '''

    def get_name(self) -> str:
        '''
        Shortcut that gets the name of the solution file.
        '''
        return self.get("name")

    def get_size(self) -> int:
        '''
        Shortcut that gets the size of the solution file in bytes.
        '''
        return self.get("size")

    def download(self, path: str):
        '''
        Downloads the solution file to the specified path.
        The path should be either a file name path or a directory path.
        In the latter case, the file will be named {solution_file_id}.
        '''
        if Path(path).is_dir():
            path = Path(path) / f"{self.get_name()}"
        elif not Path(path).parent.exists():
            raise Exception(f"Directory {Path(path).parent} does not exist")

        client = Cache.cache().get_client()
        client.send_request_by_callback(
            DefaultApi.uploaded_files_presenter_action_download,
            path_params={"id": self.id()}
        ).save_to_file(path)

    def get_content(self) -> str:
        '''
        Gets the content of the solution file as string.
        Returns dictionary {
            "content": <file content as string>
            "malformedCharacters": <boolean indicating whether there are replaced characters in the content>
            "tooLarge": <boolean indicating whether content was truncated due to large file size>
        }
        '''
        client = Cache.cache().get_client()
        return client.send_request_by_callback(
            DefaultApi.uploaded_files_presenter_action_content,
            path_params={"id": self.id()}
        ).get_payload()

    def get_digest(self) -> str:
        '''
        Gets the digest (hash) of the solution file.
        Returns dictionary {
            "digest": <file hash as string>
            "algorithm": <digest algorithm used, currently should be "sha1">
        }
        '''
        client = Cache.cache().get_client()
        return client.send_request_by_callback(
            DefaultApi.uploaded_files_presenter_action_digest,
            path_params={"id": self.id()}
        ).get_payload()


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

    def get_submissions(self) -> list[Submission]:
        '''
        Gets the list of all submissions of the solution.
        '''
        cache = Cache.cache()
        client = cache.get_client()
        submissions_data = client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_submissions,
            path_params={"id": self.id()}
        ).get_payload()
        submissions = [Submission(data) for data in submissions_data or []]
        return cache.inject(Submission, submissions)  # inject submissions into cache

    def download(self, path: str):
        '''
        Downloads the whole solution in a .zip archive to the specified path.
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

    def delete_submission(self, submission_id: str):
        '''
        Deletes given submission of the solution.
        '''
        submission_ids = self.get("submissions") or []
        if submission_id not in submission_ids:
            raise Exception(f"Submission with ID {submission_id} not found in the solution")

        cache = Cache.cache()
        client = cache.get_client()
        client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_delete_submission,
            path_params={"submissionId": submission_id}
        ).check_success()

        # make sure the entity is no longer usable
        if cache.has(Submission, submission_id):
            sub = cache.get(Submission, submission_id)
            sub.invalidate()  # invalidate the submission in the cache
            cache.remove(Submission, submission_id)  # remove the submission from the cache

        # solution needs to be refreshed to get the updated list of submissions and the last submission
        self.refresh()

    def get_comments_thread(self) -> CommentThread:
        '''
        Gets the comment thread associated with the solution.
        The thread is created when first used.
        '''
        return Cache.cache().get(CommentThread, self.id())  # ensure the thread is in the cache

    def get_files(self) -> list[SolutionFile]:
        '''
        Gets the list of files associated with the solution.
        '''
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_files,
            path_params={"id": self.id()}
        ).get_payload()
        return [SolutionFile(file_data) for file_data in data or []]

    def get_review(self) -> SolutionReview | None:
        '''
        Gets the review of the solution, or None if there is no review.
        '''
        if self.get("review", "startedAt") is None:
            return None
        return Cache.cache().get(SolutionReview, self.id())

    def start_review(self, close: bool = False) -> SolutionReview:
        '''
        Starts the review of the solution. If the review already exists, it is returned instead.
        '''
        review = self.get_review()
        if review is not None:
            return review

        review = SolutionReview({"id": self.id()})
        review.update_status(close)  # this will create the review and update its data
        return Cache.cache().inject(SolutionReview, review)  # inject the review into the cache
