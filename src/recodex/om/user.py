from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .base import BaseEntity


class User(BaseEntity):
    '''
    Wrapper for user data structure with additional features.
    '''

    def refresh(self):
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.users_presenter_action_detail,
            path_params={"id": self.id()}).get_payload()
        self.update(data)

    def get_name(self, surname_first: bool = False) -> str:
        '''
        Gets the name of the user.
        '''
        if surname_first:
            return self.get_strict("name", "lastName") + " " + self.get_strict("name", "firstName")
        return self.get_strict("name", "firstName") + " " + self.get_strict("name", "lastName")

    def get_full_name(self) -> str:
        '''
        Gets the full name of the user, including the title if available.
        '''
        return self.get_strict("fullName")

    @staticmethod
    def load_by_ids(ids: list[str]) -> list["User"]:
        '''
        Loads users by their IDs.
        '''
        cache = Cache.cache()
        client = cache.get_client()
        users_data = client.send_request_by_callback(
            DefaultApi.users_presenter_action_list_by_ids,
            body={"ids": ids}
        ).get_payload()
        users = [User(data) for data in users_data or []]
        return cache.inject(User, users)  # inject users into cache
