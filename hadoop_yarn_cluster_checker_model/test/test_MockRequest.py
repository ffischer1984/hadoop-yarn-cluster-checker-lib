import os

from MockRequest import MockRequest
from UtilsTest import UtilsTest


class TestMockRequest:
    __file_running_app = os.path.dirname(__file__) + "/res/running_app.json"
    def test_running_jobs(self):
        mock_req = MockRequest(has_internet=False, are_jobs_running=True)
        print(os.getcwd())

        with open(UtilsTest.get_file_running_app(self), "r") as successResponseBodyFile:
            expected  = successResponseBodyFile.read()
            current = mock_req.get("https://example.com")
            assert expected == current.text

    def test_empty_cluster(self):
        mock_req = MockRequest(has_internet=False, are_jobs_running=False)
        with open(UtilsTest.get_file_empty_cluster(self), "r") as successResponseBodyFile:
            expected = successResponseBodyFile.read()
            current = mock_req.get("https://example.com")
            assert expected == current.text