from config import *

folder = "删除实验"

request = [
    {
        "name": "删除指定实验",
        "method": "DELETE",
        "url": base_url + "/experiment/{{new_experiment}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {
                "data": "",
                "message": "",
                "success": True,
                "code": 0
            },
            "attr": {
                "data": "{{new_experiment}}",
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "{{new_experiment}}"
            ]
        },
    },
]
