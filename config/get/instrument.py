from config import *

folder = "获取设备"

request = [
    {
        "name": "获取指定设备",
        "method": "GET",
        "url": base_url + "/instrument/{{new_instrument}}",
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
                "{{new_instrument}}"
            ]
        },
    },
    {
        "name": "获取所有设备",
        "method": "GET",
        "url": base_url + "/instrument",
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
