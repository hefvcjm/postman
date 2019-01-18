from config import *

folder = "删除项目"

request = [
    {
        "name": "删除指定项目",
        "method": "DELETE",
        "url": base_url + "/project/{{new_project}}",
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
                "data": "{{new_project}}",
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "{{new_project}}"
            ]
        },
    },
]
