from .cache import Cache
from .base import LocalizedEntity
from .exercise import Exercise
from .solution import Solution


class Assignment(LocalizedEntity):
    '''
    Wrapper for assignment data structure with additional features.
    '''

    def get_exercise(self) -> Exercise:
        '''
        Gets the exercise of the assignment.
        '''
        id = self.get("exerciseId")
        return Cache.cache().get(Exercise, id) if id else None

    def get_solutions(self):
        '''
        Gets the list of solutions of the assignment.
        '''
        cache = Cache.cache()
        client = cache.get_client()
        solutions_data = client.send_request("assignments", "solutions",
                                             path_params={"id": self.id()}).get_payload()
        solutions = [Solution(data) for data in solutions_data]
        cache.inject(Solution, solutions)  # inject solutions into cache
        return solutions
