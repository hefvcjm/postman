# coding = utf-8
from . import *
import re
import json
import os


class Use:

    def __init__(self, setting):
        self.__setting = setting
        if "params" not in setting.keys():
            self.__setting["params"] = {}
        if "body" not in setting.keys():
            self.__setting["body"] = {}
        if "header" not in setting.keys():
            self.__setting["header"] = {}
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
            if "save" in item.keys():
                save = item["save"]
            else:
                save = None
            if "res_update" in item.keys():
                update = item["res_update"]
            else:
                update = None
            self.__pre_script.send_request(item["url"], item["method"], item["header"], item["body"], save, update)
            if "update" not in item.keys():
                continue
            for key, value in zip(item["update"].keys(), item["update"].values()):
                self.__pre_script.update_json_variable(key, value)

    def __set_request(self):
        self.__request.set_request(self.__setting["method"], self.__setting["url"], self.__setting["params"],
                                   self.__setting["header"], self.__setting["body"])

    def __set_test(self):
        if "test" in self.__setting.keys():
            test = self.__setting["test"]
            if "status_code" in test.keys():
                self.__test.test_status_code(str(test["status_code"]))
            if "response_json" in test.keys() and test["response_json"] is True:
                self.__test.test_response_json()
            if "json_schema" in test.keys():
                self.__test.test_response_schema(test["json_schema"])
            if "attr" in test.keys():
                for item in test["attr"].keys():
                    if isinstance(test["attr"][item], str) and re.match("{{.*}}", test["attr"][item].strip()):
                        self.__test.test_response_json_has_variable(item.split("."), "globals",
                                                                    test["attr"][item].replace("{", "").replace("}",
                                                                                                                ""))
                    else:
                        self.__test.test_response_json_has(item.split("."), test["attr"][item])
            if "attr_has" in test.keys():
                for item in test["attr_has"].keys():
                    if isinstance(test["attr_has"][item], str) and re.match("{{.*}}", test["attr_has"][item].strip()):
                        self.__test.test_response_json_has_variable(item.split("."), "globals",
                                                                    test["attr_has"][item].replace("{", "").replace("}",
                                                                                                                    ""),
                                                                    mode="include")
                    else:
                        self.__test.test_response_json_has(item.split("."), test["attr_has"][item], mode="include")
            if "has" in test.keys():
                for item in test["has"]:
                    if re.match("{{.*}}", item.strip()):
                        self.__test.test_has_variable("globals", item.strip().replace("{", "").replace("}", ""))
                    else:
                        self.__test.test_has_string(item)

    def __save(self):
        if "save" not in self.__setting.keys():
            return
        # print(self.__setting["save"])
        save = self.__setting["save"]
        if "json" in save.keys():
            for a, b in zip(save["json"].keys(), save["json"].values()):
                self.__test.save_response(b, a.split("."), "json")
        if "no_json" in save.keys():
            for a, b in zip(save["no_json"].keys(), save["no_json"].values()):
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


def dump_postman(folders, name="dump_postman", path=""):
    collection = Collection.Collection(name)
    for folder in folders:
        f = Folder.Folder(folder["name"])
        for request in folder["request"]:
            f.add_request(Use(request).get())
        collection.add_item(f)
    with open(os.path.join(path, name + ".json"), "w") as file:
        file.write(json.dumps(collection.get_json(), indent=4))
