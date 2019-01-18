from config import *

folder = "删除设备"

request = [
    {
        "name": "删除指定设备",
        "method": "DELETE",
        "url": base_url + "/instrument/{{new_instrument}}",
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
                "data": "{{new_instrument}}",
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "{{new_instrument}}"
            ]
        },
    },
]
