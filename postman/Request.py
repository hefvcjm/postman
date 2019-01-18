# coding = utf-8
from urllib.parse import urlparse
from .Base import *
import copy
import json


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
                "protocol": "",
                "host": [],
                "path": [],
                "query": []
            }
        }
        self._response = []

    def set_request(self, method, url, header, data):
        self._request["method"] = method
        for key in header.keys():
            self._request["header"].append(
                {"key": key, "value": header[key], "type": "text"} if key != "Content-Type"
                else {"key": key, "value": header[key], "name": key, "type": "text"})
        self._request["url"]["raw"] = url
        parsed_uri = urlparse(copy.deepcopy(url))
        self._request["url"]["protocol"] = parsed_uri.scheme
        if parsed_uri.netloc != "":
            self._request["url"]["host"] += parsed_uri.netloc.split(".")
        paths = parsed_uri.path.split("/")
        if len(paths) != 0:
            for i in paths[1:]:
                self._request["url"]["path"].append(i)
        self._request["body"]["raw"] = json.dumps(data, ensure_ascii=False) \
            .replace("True", "true").replace("False", "false") if isinstance(data, dict) else data
        if parsed_uri.query != "":
            query = parsed_uri.query.split("&")
            if len(query) != 0:
                for i in query:
                    temp = i.split("=")
                    if len(temp) != 0:
                        self._request["url"]["query"].append(
                            {"key": temp[0], "value": "" if len(temp) == 1 else temp[1]})

    def get_json(self):
        self._json = {
            "name": self._name,
            "event": self._event,
            "request": self._request,
            "response": self._response
        }
        return self._json
