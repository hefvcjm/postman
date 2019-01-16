# coding = utd-8
import uuid


class Base:

    def __init__(self, name=""):
        self._event = []
        self._json = None

    def set_pre_script(self, script):
        flag = False
        for item in self._event:
            if item["listen"] == "prerequest":
                item["script"]["exec"] = script
                flag = True
        if not flag:
            self._event.append({
                "listen": "prerequest",
                "script": {
                    "id": str(uuid.uuid4()),
                    "type": "text/javascript",
                    "exec": script
                }
            })

    def set_test_script(self, script):
        flag = False
        for item in self._event:
            if item["listen"] == "test":
                item["script"]["exec"] = script
                flag = True
        if not flag:
            self._event.append({
                "listen": "test",
                "script": {
                    "id": str(uuid.uuid4()),
                    "type": "text/javascript",
                    "exec": script
                }
            })

    def get_json(self):
        return self._json
