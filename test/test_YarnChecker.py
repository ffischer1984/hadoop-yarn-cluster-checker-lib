import pytest
import argparse
import os
import requests

from hadoop_yarn_cluster_checker import HadoopYarnClusterChecker
from hadoop_yarn_cluster_checker import MockRequest


class TestHadoopYarnClusterChecker():
    __file_path_running_apps = os.getcwd() + "\\res\\running_app.json"

    def test_str2bool_true(self):
        assert HadoopYarnClusterChecker.str2bool("T") == True
        assert HadoopYarnClusterChecker.str2bool("t") == True
        assert HadoopYarnClusterChecker.str2bool("True") == True
        assert HadoopYarnClusterChecker.str2bool("true") == True

    def test_str2bool_ex(self):
        with pytest.raises(argparse.ArgumentTypeError):
            HadoopYarnClusterChecker.str2bool("wahr") == True

    def test_findRunningJobs_no_excludes_in_resp(self):
        checker = HadoopYarnClusterChecker(
            excludes="[{\"name\": \"Zeppelin1\"}]")  # there are no applications with the prop name="Zeppelin1" (in the response)
        print(str(os.getcwd()))
        with open(self.__file_path_running_apps, "r") as successResponseBodyFile:
            xmlText = successResponseBodyFile.read()
            assert checker.areJobsRunning(xmlText) == True

    def test_running_jobs_are_excluded(self):
        checker = HadoopYarnClusterChecker(
            excludes="[{\"name\":\"Zeppelin\"}]")  # only running application is name="Zeppelin1"
        print(str(os.getcwd()))
        with open(os.getcwd() + "\\res\\running_app.json", "r") as successResponseBodyFile:
            xmlText = successResponseBodyFile.read()
            assert checker.areJobsRunning(xmlText) == False

    def event_empty(self):
        assert True == True

    """Test is succesful if event_empty is triggered"""

    def test_not_find_running_jobs(self):
        checker = HadoopYarnClusterChecker()
        checker.on_empty_cluster += self.event_empty
        mock_req = MockRequest(has_internet=False, are_jobs_running=False)
        checker.run(mock_req)

    @pytest.mark.xfail(raises=Exception)
    def test_no_server_connection(self):
        checker = HadoopYarnClusterChecker(server="htt.g")
        mock_req = MockRequest(has_internet=True, are_jobs_running=False)
        checker.run(requests)
