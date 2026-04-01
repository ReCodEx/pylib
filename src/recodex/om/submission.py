from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .base import BaseEntity
from pathlib import Path


class Submission(BaseEntity):
    '''
    Wrapper for solution's submission data structure with additional features.
    '''

    def refresh(self):
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_submission,
            path_params={"submissionId": self.id()}).get_payload(),
        self.update(data)

    def is_evaluated(self) -> bool:
        '''
        Checks if the submission is already evaluated (not pending).
        '''
        return self.get("evaluation") is not None or self.get("failure") is not None

    def is_success(self) -> bool:
        '''
        Checks if the submission was successfully evaluated (not necessarily correct).
        '''
        return self.get("evaluation") is not None

    def is_failure(self) -> bool:
        '''
        Checks if the submission is a failure (evaluation failed at backend).
        '''
        return self.get("failure") is not None

    def get_score(self) -> float | None:
        '''
        A shortcut to solution correctness (score).
        Returns the score or None if the submission is not evaluated yet or is a failure.
        '''
        return self.get("evaluation", "score")

    def download_result_archive(self, path: str):
        '''
        Downloads the submission results .zip archive to the specified path.
        The path should be either a file name path or a directory path.
        In the latter case, the file will be named {submission_id}.zip.
        '''
        client = Cache.cache().get_client()
        if Path(path).is_dir():
            path = Path(path) / f"{self.id()}.zip"
        elif not Path(path).parent.exists():
            raise Exception(f"Directory {Path(path).parent} does not exist")

        client.send_request_by_callback(
            DefaultApi.assignment_solutions_presenter_action_download_result_archive,
            path_params={"id": self.id()}
        ).save_to_file(path)
