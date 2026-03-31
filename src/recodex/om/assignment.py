from .cache import Cache
from .base import LocalizedEntity
from .exercise import Exercise


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
