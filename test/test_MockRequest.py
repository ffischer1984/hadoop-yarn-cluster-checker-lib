import os

import hadoop_yarn_cluster_checker.MockRequest


class TestMockRequest:

    def test_running_jobs(self):
        mock_req = hadoop_yarn_cluster_checker.MockRequest(has_internet=False, are_jobs_running=True)
        with open(os.getcwd()+"\\res\\running_app.xml","r") as successResponseBodyFile:
            expected  = successResponseBodyFile.read()
            current = mock_req.get("https://example.com")
            assert expected == current.text

    def test_empty_cluster(self):
        mock_req = hadoop_yarn_cluster_checker.MockRequest(has_internet=False, are_jobs_running=True)
        with open(os.getcwd()+"\\res\\empty_cluster.xml","r") as successResponseBodyFile:
            expected = successResponseBodyFile.read()
            current = mock_req.get("https://example.com")
            assert expected == current.text