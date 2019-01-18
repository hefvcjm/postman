from config import *

folder = "获取实验"

request = [
    {
        "name": "获取指定实验",
        "method": "GET",
        "url": base_url + "/experiment/{{new_experiment}}",
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
                "{{new_experiment}}"
            ]
        },
    },
    {
        "name": "获取所有实验",
        "method": "GET",
        "url": base_url + "/experiment",
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
