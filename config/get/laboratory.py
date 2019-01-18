from config import *

folder = "获取实验室"

request = [
    {
        "name": "获取指定实验室",
        "method": "GET",
        "url": base_url + "/laboratory/{{new_laboratory}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "查询成功",
            },
            "has": [
                "{{new_laboratory}}"
            ]
        },
    },
    {
        "name": "获取所有实验室",
        "method": "GET",
        "url": base_url + "/laboratory",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {
                "data": {
                    "count": 0,
                    "results": []
                },
                "message": "",
                "code": 0,
                "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "查询成功",
            },
        },
    },

]
