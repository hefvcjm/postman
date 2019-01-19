from config import *

folder = "删除节点配置"

request = [
    {
        "name": "删除指定节点配置",
        "method": "DELETE",
        "url": base_url + "/formbuilder/{{new_formbuilder}}",
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
                "data": "{{new_formbuilder}}",
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "{{new_formbuilder}}"
            ]
        },
    },
]
