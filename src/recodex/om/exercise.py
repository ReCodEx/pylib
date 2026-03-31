from .cache import Cache
from .base import LocalizedEntity
from .user import User


class Exercise(LocalizedEntity):
    '''
    Wrapper for exercise data structure with additional features.
    '''

    def get_author(self) -> User:
        '''
        Gets the author of the exercise.
        '''
        author_id = self._data.get("authorId")
        return Cache.cache().get(User, author_id) if author_id else None

    def get_admins(self) -> list[User]:
        '''
        Gets the list of admins of the exercise.
        '''
        admins_ids = self._data.get("adminsIds") or []
        return [Cache.cache().get(User, admin_id) for admin_id in admins_ids]
