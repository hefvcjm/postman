# coding = utf-8
from .Base import *


class Collection(Base):

    def __init__(self, name=""):
        super().__init__(name)
        self._info = {
            "_postman_id": str(uuid.uuid4()),
            "name": name,
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        }
        self._item = []

    def add_item(self, item):
        self._item.append(item.get_json())

    def add_items(self, items):
        for i in items:
            self.add_item(i)

    def get_json(self):
        self._json = {
            "info": self._info,
            "item": self._item,
            "event": self._event
        }
        return self._json
