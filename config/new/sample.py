from config import *

folder = "新建样品"

request = [
    {
        "name": "正常-无父样品",
        "method": "POST",
        "url": base_url + "/sample",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test sample",
            "experiment": {
                "objectId": "{{new_experiment}}"
            }
        },
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "test sample",
                "{{new_experiment}}"
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_sample"
            },
        }
    },
    {
        "name": "正常-有父样品",
        "method": "POST",
        "url": base_url + "/sample",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test sample",
            "parentId": "{{new_sample}}",
            "experiment": {
                "objectId": "{{new_experiment}}"
            }
        },
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
            },
            "has": [
                "test sample",
                "{{new_sample}}",
                "{{new_experiment}}"
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_sample2"
            },
        }
    },
]
