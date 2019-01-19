from config import *

folder = "获取节点配置"

request = [
    {
        "name": "获取指定节点配置",
        "method": "GET",
        "url": base_url + "/formbuilder/{{new_formbuilder}}",
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
                "{{new_formbuilder}}"
            ]
        },
    },
    {
        "name": "获取所有节点配置",
        "method": "GET",
        "url": base_url + "/formbuilder",
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
