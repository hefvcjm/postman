from config import *

folder = "更新项目"

request = [
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/project/{{new_project}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_project"
                    }
                },
                "res_update": {
                    "update_project": {
                        "name": "update project",
                    }
                }
            }
        ],
        "name": "更新项目名称",
        "method": "PUT",
        "url": base_url + "/project/{{new_project}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_project}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_project}}"
            },
            "has": [
                "update project",
                "{{new_project}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/project/{{new_project}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_project"
                    }
                },
                "res_update": {
                    "update_project": {
                        "startdate": "2019-01-17",
                    }
                }
            }
        ],
        "name": "更新项目开始时间",
        "method": "PUT",
        "url": base_url + "/project/{{new_project}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_project}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_project}}"
            },
            "has": [
                "update project",
                "{{new_project}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/project/{{new_project}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_project"
                    }
                },
                "res_update": {
                    "update_project": {
                        "enddate": "2019-01-28",
                    }
                }
            }
        ],
        "name": "更新项目结束时间",
        "method": "PUT",
        "url": base_url + "/project/{{new_project}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_project}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_project}}"
            },
            "has": [
                "update project",
                "{{new_project}}"
            ]
        },
    },
]
