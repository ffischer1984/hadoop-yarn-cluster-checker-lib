import requests
import os
import hadoop_yarn_cluster_checker.MockResponse
from pathlib import Path




class MockRequest:
    def __init__(self, has_internet:bool, are_jobs_running:bool):
        self.hasInternet = has_internet
        self.are_jobs_running = are_jobs_running


    def __load_xml_files(self,isJobRunning:bool):
        cwd = Path(os.getcwd())
        file_path = ""
        if isJobRunning:
            file_path = str(cwd.parent) + "\\test\\res\\running_app.json"
        else:
            file_path = str(cwd.parent) + "\\test\\res\\empty_cluster.json"
        with open(file_path, "r") as xmlFile:
            xmlText = xmlFile.read()
            return hadoop_yarn_cluster_checker.MockResponse(xmlText)

    def __load_running_jobs_xml(self):
        cwd = Path(os.getcwd())
        file_path = str(cwd.parent) + "\\test\\res\\running_app.json"
        with open(file_path, "r") as successResponseBodyFile:
            xml_text = successResponseBodyFile.read()
            return hadoop_yarn_cluster_checker.MockResponse(xml_text)

    def get(self, host):
        if self.hasInternet:
            return requests.get(host)
        return self.__load_xml_files(self.are_jobs_running)






