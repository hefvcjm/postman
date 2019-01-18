from config import *

folder = "删除样品"

request = [
    {
        "name": "删除指定样品",
        "method": "DELETE",
        "url": base_url + "/sample/{{new_sample}}",
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
                "data": "{{new_sample}}",
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "{{new_sample}}"
            ]
        },
    },
]
