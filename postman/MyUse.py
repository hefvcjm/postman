# coding = utf-8
from . import *
import re


class Use:

    def __init__(self, setting):
        self.__setting = setting
        self.__pre_script = Script.PreScript()
        self.__request = Request.Request(self.__setting["name"])
        self.__folder = None
        self.__test = Script.TestScript()
        self.__pre_send()
        self.__set_request()
        self.__set_test()
        self.__save()
        self.__update()
        self.__build()

    def __pre_send(self):
        if "pre_send" not in self.__setting.keys():
            return
        pre_send = self.__setting["pre_send"]
        for item in pre_send:
            self.__pre_script.send_request(item["url"], item["method"], item["header"], item["body"],
                                           list(item["save"].values()), list(item["save"].keys()))
            if "update" not in item.keys():
                continue
            for key, value in zip(item["update"].keys(), item["update"].values()):
                self.__pre_script.update_json_variable(key, value)

    def __set_request(self):
        self.__request.set_request(self.__setting["method"], self.__setting["url"], self.__setting["header"],
                                   self.__setting["body"])

    def __set_test(self):
        test = self.__setting["test"]
        self.__test.test_status_code(str(test["status_code"]))
        self.__test.test_response_json()
        self.__test.test_response_schema(test["json_schema"])
        for item in test["attr"].keys():
            if isinstance(test["attr"][item], str) and re.match("{{.*}}", test["attr"][item].strip()):
                self.__test.test_response_json_has_variable(item.split("."), "env",
                                                            test["attr"][item].replace("{", "").replace("}", ""))
            else:
                self.__test.test_response_json_has(item.split("."), test["attr"][item])
        if "has" in test.keys():
            for item in test["has"]:
                if re.match("{{.*}}", item.strip()):
                    self.__test.test_has_variable("env", item.strip().replace("{", "").replace("}", ""))
                else:
                    self.__test.test_has_string(item)

    def __save(self):
        if "save" not in self.__setting.keys():
            return
        save = self.__setting["save"]
        for a, b in zip(save.keys(), save.values()):
            self.__test.save_response(b, a.split("."))

    def __update(self):
        if "update" not in self.__setting.keys():
            return
        for key, value in zip(self.__setting["update"].keys(), self.__setting["update"].values()):
            self.__test.update_json_variable(key, value)

    def __build(self):
        self.__request.set_pre_script(self.__pre_script)
        self.__request.set_test_script(self.__test)
        if "folder" in self.__setting.keys():
            self.__folder = Folder.Folder(self.__setting["folder"])
            self.__folder.add_request(self.__request)

    def get(self):
        if self.__folder is not None:
            return self.__folder
        return self.__request