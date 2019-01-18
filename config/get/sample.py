from config import *

folder = "获取样品"

request = [
    {
        "name": "获取指定样品",
        "method": "GET",
        "url": base_url + "/sample/{{new_sample}}",
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
                "{{new_sample}}"
            ]
        },
    },
    {
        "name": "获取所有样品",
        "method": "GET",
        "url": base_url + "/sample",
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
