from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .base import BaseEntity, LocalizedEntity
from .user import User
import datetime


class Comment:
    '''
    A structure that wraps one comment for simpler access to its data.
    '''

    def __init__(self, data: dict):
        self.id = data.get("id")
        self.thread_id = data.get("commentThreadId")
        self.text = data.get("text")
        self.is_private = data.get("isPrivate")
        self.posted_at = datetime.datetime.fromtimestamp(data.get("postedAt"), BaseEntity.default_timezone)
        self.user_id = (data.get("user") or {}).get("id")
        self.user_name = (data.get("user") or {}).get("name")

    def get_user(self):
        '''
        Gets the user who posted the comment.
        '''
        return Cache.cache().get(User, self.user_id) if self.user_id else None


class CommentThread(LocalizedEntity):
    '''
    Wrapper for comment thread and its features.
    '''

    def refresh(self):
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.comments_presenter_action_default,
            path_params={"id": self.id()}).get_payload()
        self.update(data)

    def get_comments(self) -> list[Comment]:
        '''
        Gets the list of comments wrapped in Comment objects.
        '''
        return [Comment(comment_data) for comment_data in self._data.get("comments", [])]

    def add_comment(self, text: str, private: bool = False):
        '''
        Adds a comment to the thread with the specified text and privacy setting.
        The comment will be added by the current user (associated with the auth token).
        '''
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.comments_presenter_action_add_comment,
            path_params={"id": self.id()},
            body={"text": text, "isPrivate": private}
        ).get_payload()
        self._data["comments"].append(data)  # add the new comment to the thread's data

    def delete_comment(self, comment_id: str):
        '''
        Deletes a comment from the thread by its ID.
        The comment will be deleted if the user is authorized to do so (e.g., if he is the author)
        '''
        client = Cache.cache().get_client()
        client.send_request_by_callback(
            DefaultApi.comments_presenter_action_delete,
            path_params={"id": self.id(), "commentId": comment_id}
        ).check_success()

        # remove the deleted comment from the thread's data
        self._data["comments"] = [comment for comment in self._data.get(
            "comments", []) if comment.get("id") != comment_id]
