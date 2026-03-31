from .cache import Cache
from .base import BaseEntity
from .user import User
from pathlib import Path


class Solution(BaseEntity):
    '''
    Wrapper for assignment's solution data structure with additional features.
    '''

    def get_author(self):
        '''
        Gets the author of the solution.
        '''
        author_id = self._data.get("authorId")
        return Cache.cache().get(User, author_id) if author_id else None

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
        response = client.send_request("assignment_solutions", "download_solution_archive",
                                       path_params={"id": self.id()})
        response.save_to_file(path)
