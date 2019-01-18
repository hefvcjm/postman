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
                "res_update": {
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
                "res_update": {
                    "update_experiment": {
                        "foldername": "update experiment",
                    }
                }
            }
        ],
        "name": "更新实验文件夹名称",
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
                "res_update": {
                    "update_experiment": {
                        "path": "update experiment",
                    }
                }
            }
        ],
        "name": "更新实验路径",
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
                "res_update": {
                    "update_experiment": {
                        "name": "update experiment",
                    }
                }
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
                        "data.objectId": "update_experiment_project"
                    }
                },
                "res_update": {
                    "update_experiment": {
                        "project.objectId": "{{update_experiment_project}}",
                    }
                }
            }
        ],
        "name": "更新实验项目",
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
                "res_update": {
                    "update_experiment": {
                        "name": "update experiment",
                    }
                }
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
                        "data.objectId": "update_experiment_instrument"
                    }
                },
                "res_update": {
                    "update_experiment": {
                        "project.objectId": "{{update_experiment_instrument}}",
                    }
                }
            }
        ],
        "name": "更新实验设备",
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
