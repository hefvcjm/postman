from config import *

folder = "新建用户"

request = [
    {
        "name": "正常",
        "method": "POST",
        "url": base_url + "/user",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "username": "hef",
            "password": "xA123456",
            "name": "黄恩芳",
            "sex": 0,
            "birth": "1999-09-09",
            "phone": "15802918993",
            "email": "hef@mkapp.com",
            "addr": "shanxi",
            "enable": True,
            "admin": False,
            "dept": "test dept",
            "title": "test title",
            "usertoken": "{{token}}"
        },
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "test dept",
                "test title",
                "hef@mkapp.com",
                "黄恩芳"
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_user"
            },
        }
    },
]
