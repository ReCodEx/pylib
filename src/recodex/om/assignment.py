from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .comments import CommentThread
from .base import LocalizedEntity
from .exercise import Exercise
from .solution import Solution


class Assignment(LocalizedEntity):
    '''
    Wrapper for assignment data structure with additional features.
    '''

    def refresh(self):
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.assignments_presenter_action_detail,
            path_params={"id": self.id()}).get_payload()
        self.update(data)

    def get_exercise(self) -> Exercise:
        '''
        Gets the exercise of the assignment.
        '''
        id = self.get("exerciseId")
        return Cache.cache().get(Exercise, id) if id else None

    def get_solutions(self) -> list[Solution]:
        '''
        Gets the list of solutions of the assignment.
        '''
        cache = Cache.cache()
        client = cache.get_client()
        solutions_data = client.send_request_by_callback(
            DefaultApi.assignments_presenter_action_solutions,
            path_params={"id": self.id()}
        ).get_payload()
        solutions = [Solution(data) for data in solutions_data]
        return cache.inject(Solution, solutions)  # inject solutions into cache

    def get_comments_thread(self) -> CommentThread:
        '''
        Gets the comment thread associated with the assignment.
        The thread is created when first used.
        '''
        return Cache.cache().get(CommentThread, self.id())  # ensure the thread is in the cache
