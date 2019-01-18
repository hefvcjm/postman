from config import *

folder = "更新样品"

request = [
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/sample/{{new_sample}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_sample"
                    }
                },
                "res_update": {
                    "update_sample": {
                        "name": "update sample",
                    }
                }
            }
        ],
        "name": "更新样品名称",
        "method": "PUT",
        "url": base_url + "/sample/{{new_sample}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_sample}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_sample}}"
            },
            "has": [
                "update sample",
                "{{new_sample}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/sample/{{new_sample}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_sample"
                    }
                },
            },
            {
                "method": "POST",
                "url": base_url + "/sample",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {
                    "name": "temp sample",
                    "experiment": {
                        "objectId": "{{new_experiment}}"
                    }
                },
                "save": {
                    "no_json": {
                        "data.objectId": "update_sample_sample"
                    }
                },
                "res_update": {
                    "update_sample": {
                        "parentId": "{{update_sample_sample}}",
                    }
                }
            }
        ],
        "name": "更新样品父样品",
        "method": "PUT",
        "url": base_url + "/sample/{{new_sample}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_sample}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_sample}}",
                "data.parentId": "{{update_sample_sample}}"
            },
            "has": [
                "update sample",
                "{{new_sample}}",
                "{{update_sample_sample}}"
            ]
        },
    },
    {
        "pre_send": [
            {
                "method": "GET",
                "url": base_url + "/sample/{{new_sample}}",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {},
                "save": {
                    "json": {
                        "data": "update_sample"
                    }
                },
            },
            {
                "method": "POST",
                "url": base_url + "/experiment",
                "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
                "body": {
                    "name": "test experiment",
                    "foldername": "test experiment",
                    "path": "test experiment",
                    "project": {
                        "objectId": "{{new_project}}"
                    },
                    "instrument": {
                        "objectId": "{{new_instrument}}"
                    }
                },
                "save": {
                    "no_json": {
                        "data.objectId": "update_sample_experiment"
                    }
                },
                "res_update": {
                    "update_sample": {
                        "experiment": {
                            "objectId": "{{update_sample_experiment}}"
                        },
                    }
                }
            }
        ],
        "name": "更新样品关联实验",
        "method": "PUT",
        "url": base_url + "/sample/{{new_sample}}",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": "{{update_sample}}",
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "执行成功",
                "data.objectId": "{{new_sample}}",
                "data.experiment.parentId": "{{update_sample_experiment}}"
            },
            "has": [
                "update sample",
                "{{new_sample}}",
                "{{update_sample_experiment}}"
            ]
        },
    },
]
