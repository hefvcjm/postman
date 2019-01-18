from config import *

folder = "删除实验室"

request = [
    {
        "name": "删除指定实验室",
        "method": "DELETE",
        "url": base_url + "/laboratory/{{new_laboratory}}",
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
                "data": "{{new_laboratory}}",
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "{{new_laboratory}}"
            ]
        },
    },
]
