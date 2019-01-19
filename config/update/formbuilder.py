from config import *

folder = "更新节点配置"

request = [
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/formbuilder/{{new_formbuilder}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_formbuilder"
                    }
                },
            },
            {
                "method": "POST",
                "url": base_url + "/project",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {
                    "name": "temp project",
                    "startdate": "2019-01-18",
                    "enddate": "2019-01-25"
                },
                "save": {
                    "no_json": {
                        "data.objectId": "update_formbuilder_project"
                    }
                },
                "res_update": {
                    "update_formbuilder": {
                        "project.objectId": "{{update_formbuilder_project}}",
                    }
                }
            }
        ],
        "name": "更新节点配置项目",
        "method": "PUT",
        "url": base_url + "/formbuilder/{{new_formbuilder}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_formbuilder}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_formbuilder}}"
            },
            "has": [
                "{{update_formbuilder_project}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/formbuilder/{{new_formbuilder}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_formbuilder"
                    }
                },
            },
            {
                "method": "POST",
                "url": base_url + "/instrument",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {
                    "name": "test instrument",
                    "foldername": "test instrument",
                },
                "save": {
                    "no_json": {
                        "data.objectId": "update_formbuilder_instrument"
                    }
                },
                "res_update": {
                    "update_formbuilder": {
                        "instrument.objectId": "{{update_formbuilder_instrument}}",
                    }
                }
            }
        ],
        "name": "更新节点配置设备",
        "method": "PUT",
        "url": base_url + "/formbuilder/{{new_formbuilder}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_formbuilder}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_formbuilder}}"
            },
            "has": [
                "{{update_formbuilder_instrument}}"
            ]
        },
    },
]
