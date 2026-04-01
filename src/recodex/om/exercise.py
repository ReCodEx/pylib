from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .base import LocalizedEntity
from .user import User


class Exercise(LocalizedEntity):
    '''
    Wrapper for exercise data structure with additional features.
    '''

    def refresh(self):
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.exercises_presenter_action_detail,
            path_params={"id": self.id()}).get_payload()
        self.update(data)

    def get_author(self) -> User:
        '''
        Gets the author of the exercise.
        '''
        author_id = self.get("authorId")
        return Cache.cache().get(User, author_id) if author_id else None

    def get_admins(self) -> list[User]:
        '''
        Gets the list of admins of the exercise.
        '''
        admins_ids = self.get("adminsIds") or []
        return [Cache.cache().get(User, admin_id) for admin_id in admins_ids]
