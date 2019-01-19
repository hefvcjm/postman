# coding = utf-8
import json
from postman.Use import *

# 登录和注销
from config.login_out import *

test_list = [logout, login]

# 新建
from config.new import *

test_list += [instrument, laboratory, project, experiment, sample, formbuilder]

# 查询
from config.get import *

test_list += [instrument, laboratory, project, experiment, sample, formbuilder]

# 更新
from config.update import *

test_list += [experiment, instrument, laboratory, project, sample, formbuilder]

# 删除
from config.delete import *

test_list += [experiment, instrument, laboratory, project, sample, formbuilder]

folders = []
for item in test_list:
    folders.append({"name": item.folder, "request": item.request})
if __name__ == '__main__':
    collection = Collection.Collection("MatdataAPI")
    for folder in folders:
        f = Folder.Folder(folder["name"])
        for request in folder["request"]:
            f.add_request(Use(request).get())
        collection.add_item(f)
    with open(r"C:\Users\win10\Desktop\MatdataAPI.postman_collection.json", "w") as file:
        file.write(json.dumps(collection.get_json(), indent=4))
