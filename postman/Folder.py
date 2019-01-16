# coding = utf-8
from .Base import *


class Folder(Base):

    def __init__(self, name=""):
        super().__init__(name)
        self._name = name
        self._item = []

    def add_request(self, request):
        self._item.append(request.get_json())

    def add_requests(self, requests):
        for item in requests:
            self.add_request(item)

    def get_json(self):
        self._json = {
            "name": self._name,
            "item": self._item,
            "event": self._event
        }
        return self._json
