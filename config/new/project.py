from config import *

folder = "新建项目"

request = [
    {
        "name": "正常",
        "method": "POST",
        "url": base_url + "/project",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test project",
            "startdate": "2019-01-18",
            "enddate": "2019-01-25"
        },
        "test": {
            "status_code": 200,
            "json_schema": {
                "data": {
                    "objectId": "",
                    "locktime": 0,
                    "createDate": "",
                    "updateDate": "",
                    "createUser": "",
                    "updateUser": "",
                    "name": "",
                    "startdate": "",
                    "enddate": "",
                    "participants": [],
                    "scope": 0,
                    "finish": False
                },
                "message": "执行成功",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功"
            },
            "has": [
                "test project",
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_project"
            }
        }
    },
    {
        "name": "名字为空",
        "method": "POST",
        "url": base_url + "/project",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "",
            "startdate": "2019-01-18",
            "enddate": "2019-01-25"
        },
        "test": {
            "status_code": 200,
            "json_schema": {
                "data": {
                    "objectId": "",
                    "locktime": 0,
                    "createDate": "",
                    "updateDate": "",
                    "createUser": "",
                    "updateUser": "",
                    "name": "",
                    "startdate": "",
                    "enddate": "",
                    "participants": [],
                    "scope": 0,
                    "finish": False
                },
                "message": "执行成功",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功"
            },
        },
    },
]
