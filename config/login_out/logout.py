from config import *

# 所属文件夹名称
folder = "注销"

# 请求集合
request = [
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/user/login?username=administrator&password=xA123456",
                "header": {"Content-Type": "application/json"},
                "body": {},
                "save": {
                    "no_json": {
                        "data.username": "user",
                        "data.usertoken": "token",
                        "data.objectId": "user_objectId"
                    },
                },
            }
        ],
        "name": "正常注销",
        "method": "GET",
        "url": base_url + "/user/logout?username={{user}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {
                "message": "",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "查询成功",
            },
        },
    },
]
