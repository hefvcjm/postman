# coding = utf-8
from urllib.parse import urlparse
from .Base import *


class Request(Base):

    def __init__(self, name=""):
        super().__init__(name)
        self._name = name
        self._request = {
            "method": "GET",
            "header": [],
            "body": {
                "mode": "raw",
                "raw": ""
            },
            "url": {
                "raw": "",
                "host": [],
                "path": []
            }
        }
        self._response = []

    def set_request(self, method, url, header, data):
        self._request["method"] = method
        for key in header.keys():
            self._request["header"].append({"key": key, "value": header[key], "type": "text"})
        self._request["url"]["raw"] = url
        parsed_uri = urlparse(url)
        self._request["url"]["host"].append(parsed_uri.netloc if parsed_uri.netloc != "" else "")
        paths = parsed_uri.path.split("/")
        if len(paths) != 0:
            for i in paths[1:]:
                self._request["url"]["path"].append(i)
        self._request["body"]["raw"] = str(data)

    def get_json(self):
        self._json = {
            "name": self._name,
            "event": self._event,
            "request": self._request,
            "response": self._response
        }
        return self._json
