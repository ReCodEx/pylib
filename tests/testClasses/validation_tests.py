from jsonschema.exceptions import ValidationError

from recodex.generated.swagger_client.api.default_api import DefaultApi

from .test_class_base import TestClassBase

from ..utils import constants


class ValidationTests(TestClassBase):
    def test_invalid_body(self):
        def request(): return self.client.send_request_by_callback(
            DefaultApi.registration_presenter_action_create_invitation,
            body={
                "email": "name@domain.tld",
                "firstName": "text",
                "lastName": "text",
                "instanceId": constants.uuid,
                "titlesBeforeName": "text",
                "titlesAfterName": "text",
                "groups": [
                    "string"
                ],
                "locale": "THIS TEXT IS TOO LONG",
                "ignoreNameCollision": True
            },
        ).get_parsed_data()

        self.assertRaises(ValidationError, request)

    def test_valid_body(self):
        res = self.client.send_request_by_callback(
            DefaultApi.registration_presenter_action_create_invitation,
            body={
                "email": "name@domain.tld",
                "firstName": "text",
                "lastName": "text",
                "instanceId": constants.uuid,
                "titlesBeforeName": "text",
                "titlesAfterName": "text",
                "groups": [
                    "string"
                ],
                "locale": "en",
                "ignoreNameCollision": True
            },
        ).get_parsed_data()

        self.assertTrue(res)
