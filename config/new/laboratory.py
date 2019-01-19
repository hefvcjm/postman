from config import *

folder = "新建实验室"

request = [
    {
        "name": "正常",
        "method": "POST",
        "url": base_url + "/laboratory",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test laboratory",
            "foldername": "test laboratory",
            "instruments": ["{{new_instrument}}"]
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
                    "foldername": "",
                    "children": [],
                    "instruments": []
                },
                "message": "",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功"
            },
            "has": [
                "test laboratory",
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_laboratory"
            }
        }
    },
    {
        "name": "空设备列表",
        "method": "POST",
        "url": base_url + "/laboratory",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test laboratory",
            "foldername": "test laboratory",
            "instruments": []
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
                    "foldername": "",
                    "children": [],
                    "instruments": []
                },
                "message": "",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功"
            },
            "has": [
                "test laboratory",
            ]
        },
    },
    {
        "name": "设备不存在",
        "method": "POST",
        "url": base_url + "/laboratory",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test laboratory",
            "foldername": "test laboratory",
            "instruments": ["5c40b30a45581e2dce854e22d"]
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
                    "foldername": "",
                    "children": [],
                    "instruments": []
                },
                "message": "",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功"
            },
            "has": [
                "test laboratory",
            ]
        },
    },
    {
        "name": "名称为空",
        "method": "POST",
        "url": base_url + "/laboratory",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "",
            "foldername": "test laboratory",
            "instruments": ["{{new_instrument}}"]
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
                    "foldername": "",
                    "children": [],
                    "instruments": []
                },
                "message": "",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功"
            },
            "has": [
                "test laboratory",
            ]
        },
    },
    {
        "name": "路径为空",
        "method": "POST",
        "url": base_url + "/laboratory",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test laboratory",
            "foldername": "",
            "instruments": ["{{new_instrument}}"]
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
                    "foldername": "",
                    "children": [],
                    "instruments": []
                },
                "message": "",
                "success": True,
                "code": 0
            },
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功"
            },
            "has": [
                "test laboratory",
            ]
        },
    },
]
