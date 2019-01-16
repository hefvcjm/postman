# coding = utf-8
from postman import *
import json

if __name__ == '__main__':
    login = Request.Request("login")
    login.set_request("GET", "http://39.104.25.189:8188/matdata/v1/user/login?username=administrator&password=xA123456",
                      {"Content-Type": "json/application"}, {"username": "administrator", "password": "xA123456"})
    print(login.get_json())
    script = Script.PreScript()
    script.set_global_environment("test", "test")
    script.send_request("http://39.104.25.189:8188/matdata/v1/user/login", "POST",
                        str({"Content-type": "json/application"}), str({"test": "test"}), "")
    login.set_pre_script(script.get_script())
    login.set_test_script(script.get_script())
    folder = Folder.Folder("test")
    folder.add_request(login)
    folder.set_pre_script(script.get_script())
    folder.set_test_script(script.get_script())
    collection = Collection.Collection("hefvcjm")
    collection.add_item(login)
    collection.add_item(folder)
    collection.set_pre_script(script.get_script())
    collection.set_test_script(script.get_script())
    with open("hefvcjm.postman_collection.json", "w") as file:
        file.write(json.dumps(collection.get_json(), indent=4))
