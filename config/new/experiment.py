from config import *

folder = "新建实验"

request = [
    {
        "name": "正常",
        "method": "POST",
        "url": base_url + "/experiment",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test experiment",
            "foldername": "test experiment",
            "path": "test experiment",
            "project": {
                "objectId": "{{new_project}}",
            },
            "instrument": {
                "objectId": "{{new_instrument}}"
            }
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
                "test experiment",
                "{{new_project}}",
                "{{new_instrument}}"
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_experiment"
            },
        }
    },
]
