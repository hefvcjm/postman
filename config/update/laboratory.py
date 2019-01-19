from config import *

folder = "更新实验室"

request = [
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/laboratory/{{new_laboratory}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_laboratory"
                    }
                },
                "res_update": {
                    "update_laboratory": {
                        "name": "update laboratory",
                    }
                }
            }
        ],
        "name": "更新实验室名称",
        "method": "PUT",
        "url": base_url + "/laboratory/{{new_laboratory}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_laboratory}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_laboratory}}"
            },
            "has": [
                "update laboratory",
                "{{new_laboratory}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/laboratory/{{new_laboratory}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_laboratory"
                    }
                },
                "res_update": {
                    "update_laboratory": {
                        "foldername": "update laboratory",
                    }
                }
            }
        ],
        "name": "更新实验室文件夹名称",
        "method": "PUT",
        "url": base_url + "/laboratory/{{new_laboratory}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_laboratory}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_laboratory}}"
            },
            "has": [
                "update laboratory",
                "{{new_laboratory}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/laboratory/{{new_laboratory}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_laboratory"
                    }
                },
            },
            {
                "method": "POST",
                "url": base_url + "/instrument",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {
                    "name": "temp instrument",
                    "foldername": "temp instrument",
                },
                "save": {
                    "json": {
                        "data": "update_laboratory_instrument"
                    },
                    "no_json": {
                        "data.objectId": "temp_instrument"
                    }
                },
                "res_update": {
                    "update_laboratory": {
                        "instruments": ["{{new_instrument}}", "{{temp_instrument}}"],
                    }
                }
            }
        ],
        "name": "更新实验室设备列表",
        "method": "PUT",
        "url": base_url + "/laboratory/{{new_laboratory}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_laboratory}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_laboratory}}"
            },
            "has": [
                "update laboratory",
                "{{new_laboratory}}"
            ]
        },
    },
]
