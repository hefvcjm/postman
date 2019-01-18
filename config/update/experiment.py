from config import *

folder = "更新实验"

request = [
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/experiment/{{new_experiment}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_experiment"
                    }
                },
                "update": {
                    "update_experiment": {
                        "name": "update experiment",
                    }
                }
            }
        ],
        "name": "更新实验名称",
        "method": "PUT",
        "url": base_url + "/experiment/{{new_experiment}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_experiment}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "查询成功",
                "data.objectId": "{{new_experiment}}"
            },
            "has": [
                "update experiment",
                "{{new_experiment}}"
            ]
        },
    },

]
