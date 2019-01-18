from config import *

folder = "更新设备"

request = [
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/instrument/{{new_instrument}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_instrument"
                    }
                },
                "res_update": {
                    "update_instrument": {
                        "name": "update instrument",
                    }
                }
            }
        ],
        "name": "更新设备名称",
        "method": "PUT",
        "url": base_url + "/instrument/{{new_instrument}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_instrument}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_instrument}}"
            },
            "has": [
                "update instrument",
                "{{new_instrument}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/instrument/{{new_instrument}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_instrument"
                    }
                },
                "res_update": {
                    "update_instrument": {
                        "foldername": "update instrument",
                    }
                }
            }
        ],
        "name": "更新设备文件夹名称",
        "method": "PUT",
        "url": base_url + "/instrument/{{new_instrument}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_instrument}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_instrument}}"
            },
            "has": [
                "update instrument",
                "{{new_instrument}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/instrument/{{new_instrument}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_instrument"
                    }
                },
                "res_update": {
                    "update_instrument": {
                        "formconfig": "",
                    }
                }
            }
        ],
        "name": "更新设备配置信息",
        "method": "PUT",
        "url": base_url + "/instrument/{{new_instrument}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_instrument}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_instrument}}"
            },
            "has": [
                "update instrument",
                "{{new_instrument}}"
            ]
        },
    },
]
