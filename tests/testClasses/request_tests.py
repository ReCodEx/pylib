from recodex_cli_lib.helpers.file_upload_helper import upload
from recodex_cli_lib.generated.swagger_client.api.default_api import DefaultApi

from .test_class_base import TestClassBase

from ..utils import constants


class RequestTests(TestClassBase):
    # test the send_request method on the groups.default endpoint
    def test_get_groups_info(self):
        res = self.client.send_request("groups", "default").get_parsed_data()
        self.assertNotEqual(res, None)
        self.assertEqual(res["payload"][0]["id"], constants.uuid)  # type: ignore

    # test the send_request_by_callback method on the groups.default endpoint
    def test_get_groups_info_callback(self):
        res = self.client.send_request_by_callback(DefaultApi.groups_presenter_action_default).get_parsed_data()
        self.assertNotEqual(res, None)
        self.assertEqual(res["payload"][0]["id"], constants.uuid)  # type: ignore

    # test the file upload utility function
    def test_upload_file(self):
        id = upload(self.client, "tests/utils/uploadTestFile.txt")
        self.assertEqual(id, constants.uuid)
