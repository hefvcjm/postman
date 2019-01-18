# coding = utf-8
import json
from postman.Use import *
from config.login_out import *
from config.new import *

test_list = [logout, login, instrument, laboratory, project, experiment, sample]
folders = []
for item in test_list:
    folders.append({"name": item.folder, "reequest": item.request})
if __name__ == '__main__':
    collection = Collection.Collection("hefvcjm")
    for folder in folders:
        f = Folder.Folder(folder["name"])
        for request in folder["request"]:
            f.add_request(Use(request).get())
        collection.add_item(f)
    with open(r"C:\Users\win10\Desktop\hefvcjm.postman_collection.json", "w") as file:
        file.write(json.dumps(collection.get_json(), indent=4))
