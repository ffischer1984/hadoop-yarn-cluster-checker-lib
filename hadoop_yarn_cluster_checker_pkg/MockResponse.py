import requests

class MockResponse(requests.Response):
    text = ""
    def __init__(self,text):
        self.text = text