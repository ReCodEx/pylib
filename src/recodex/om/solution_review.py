from recodex.generated.swagger_client import DefaultApi
from .cache import Cache
from .base import BaseEntity
from .user import User


class ReviewComment:
    '''
    Wrapper for review comment data structure.
    '''

    def __init__(self, data: dict, review: "SolutionReview"):
        self.id = data["id"]
        self.author_id = data["author"]
        self.created_at = data["createdAt"]
        self.file = data["file"]
        self.line = data["line"]
        self.text = data["text"]
        self.issue = data["issue"]
        self.review = review

    def get_author(self) -> User:
        '''
        Gets the author of the comment.
        '''
        return Cache.cache().get(User, self.author_id) if self.author_id else None

    def save(self, suppress_notification: bool = False):
        '''
        Saves the comment changes. Only text and issue can be changed.
        If `suppress_notification` is True, no email notification will be sent to the solution author about the change.
        Notifications are sent only if the review is already closed (so the author can see the comments).
        '''
        client = Cache.cache().get_client()
        client.send_request_by_callback(
            DefaultApi.assignment_solution_reviews_presenter_action_edit_comment,
            path_params={"id": self.review.id(), "commentId": self.id},
            body={
                "text": self.text,
                "issue": self.issue,
                "suppressNotification": suppress_notification
            }
        ).check_success()

    def delete(self):
        '''
        Deletes the comment.
        '''
        client = Cache.cache().get_client()
        client.send_request_by_callback(
            DefaultApi.assignment_solution_reviews_presenter_action_delete_comment,
            path_params={"id": self.review.id(), "commentId": self.id}
        ).check_success()
        self.review._comments = [comment for comment in self.review._comments if comment.id != self.id]


class SolutionReview(BaseEntity):
    '''
    Wrapper for solution review data structure.
    '''

    def update(self, data):
        '''
        This update is tricky as the endpoints return both review and solution data.
        Furthermore, the review must copy its ID from the solution.
        '''
        solution_data = data.pop("solution")
        data["id"] = solution_data["id"]  # copy ID from the solution
        super().update(data)
        Cache.cache().update_raw("Solution", solution_data)
        self._comments = [ReviewComment(comment_data, self) for comment_data in data.get("comments", [])]

    def invalidate(self):
        super().invalidate()
        self._comments = None

    def refresh(self):
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.assignment_solution_reviews_presenter_action_default,
            path_params={"id": self.id()}).get_payload()
        self.update(data)

    def update_status(self, close: bool):
        '''
        Update the status of the review. If no review exist yet, it will be created.
        The `close` parameter indicates whether the review should be closed (finalized) or not.
        '''
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.assignment_solution_reviews_presenter_action_update,
            path_params={"id": self.id()},
            body={"close": close}
        ).get_payload()
        self.update(data)

    def remove(self):
        '''
        Removes the review. The entity is invalidated and removed from the cache, so it can no longer be used.
        '''
        cache = Cache.cache()
        client = cache.get_client()
        client.send_request_by_callback(
            DefaultApi.assignment_solution_reviews_presenter_action_remove,
            path_params={"id": self.id()}
        ).check_success()

        # remove the review from the cache and invalidate it
        cache.remove(SolutionReview, self.id())
        self.invalidate()

    def get_comments(self) -> list[ReviewComment]:
        '''
        Gets the list of comments in the review.
        '''
        return self._comments

    def add_comment(self, file: str, line: int, text: str, issue: bool, suppress_notification: bool = False):
        '''
        Creates a new comment in the review.
        If `suppress_notification` is True, no email notification will be sent to the solution author.
        Notifications are sent only if the review is already closed (so the author can see the comments).
        '''
        client = Cache.cache().get_client()
        data = client.send_request_by_callback(
            DefaultApi.assignment_solution_reviews_presenter_action_new_comment,
            path_params={"id": self.id()},
            body={
                "text": text,
                "file": file,
                "line": line,
                "issue": issue,
                "suppressNotification": suppress_notification
            }
        ).get_payload()
        self._comments.append(ReviewComment(data, self))
