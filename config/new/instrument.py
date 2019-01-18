from config import *

# 所属文件夹名称
folder = "新建设备"

request = [
    {
        "name": "正常-带formconfig",
        "method": "POST",
        "url": base_url + "/instrument",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test instrument",
            "foldername": "test instrument",
            "formconfig": str([
                {"component": "textArea", "editable": True, "index": 0, "label": "笔记", "description": "",
                 "placeholder": "请输入...", "options": [], "options2": [], "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:742"},
                {"component": "radio", "editable": True, "index": 1, "label": "材料类型", "description": "",
                 "placeholder": "placeholder", "options": ["金属块体", "薄膜", "生物样品", "其他"], "options2": [],
                 "options3": [], "required": False, "validation": "/.*/", "$$hashKey": "object:684"},
                {"component": "textArea", "editable": True, "index": 2, "label": "加工历史", "description": "",
                 "placeholder": "请输入...", "options": [], "options2": [], "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:755"},
                {"component": "radio", "editable": True, "index": 3, "label": "压头形状", "description": "",
                 "placeholder": "placeholder", "options": ["berkovich", "立方锥角", "圆锥", "平压头", "其他"],
                 "options2": [], "options3": [], "required": False, "validation": "/.*/",
                 "$$hashKey": "object:431"},
                {"component": "radio", "editable": True, "index": 4, "label": "压头材料", "description": "",
                 "placeholder": "placeholder", "options": ["金刚石", "蓝宝石", "钨", "其他"], "options2": [],
                 "options3": [], "required": False, "validation": "/.*/", "$$hashKey": "object:382"},
                {"component": "textArea", "editable": True, "index": 5, "label": "组织特征", "description": "",
                 "placeholder": "请输入...", "options": [], "options2": [], "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:806"},
                {"component": "textInput", "editable": True, "index": 6, "label": "屈服强度",
                 "description": "MPa", "placeholder": "请输入....", "options": [], "options2": [],
                 "options3": [], "required": False, "validation": "[number]", "$$hashKey": "object:779"},
                {"component": "thirdcascapeselect", "editable": True, "index": 7, "label": "样品尺寸",
                 "description": "", "placeholder": "请输入值...", "options": ["立方体", "柱体", "球体", "其他"],
                 "options2": {"选项一": ["二级选项一11", "二级选项二11"], "选项二": ["二级选项一22", "二级选项二22"], "null": [],
                              "立方体": ["长", "宽", "高"], "柱体": ["直径", "高度"], "球体": ["半径"], "其他": ["其他"]},
                 "options3": {"二级选项一11": ["三级单位一111", "三级单位二111"], "二级选项二11": ["三级单位一112", "三级单位二112"],
                              "二级选项一22": ["三级单位一221", "三级单位二221"], "二级选项二22": ["三级单位一222", "三级单位二222"],
                              "undefined": [], "长": ["nm/μm"], "宽": ["nm/μm"], "高": ["nm/μm"], "null": [],
                              "直径": ["nm/μm"], "高度": ["nm/μm"], "半径": ["nm/μm"], "其他": ["无"]},
                 "required": False, "validation": "/.*/", "$$hashKey": "object:305"},
                {"component": "thirdcascapeselect", "editable": True, "index": 8, "label": "加载方式",
                 "description": "", "placeholder": "请输入值...", "options": ["力控制", "位移控制"],
                 "options2": {"选项一": ["二级选项一11", "二级选项二11"], "选项二": ["二级选项一22", "二级选项二22"], "null": [],
                              "力控制": ["加载速率", "最大载荷"], "位移控制": ["加载速率", "最大载荷"]},
                 "options3": {"二级选项一11": ["三级单位一111", "三级单位二111"], "二级选项二11": ["三级单位一112", "三级单位二112"],
                              "二级选项一22": ["三级单位一221", "三级单位二221"], "二级选项二22": ["三级单位一222", "三级单位二222"],
                              "undefined": [], "加载速率": ["nN"], "最大载荷": ["nN"]}, "required": False,
                 "validation": "/.*/", "$$hashKey": "object:343"}]),
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
                    "isassign": False,
                    "foldername": "",
                    "formconfig": ""
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
                "test instrument",
                "component"
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_instrument"
            }
        }
    },
    {
        "name": "正常-不带formconfig",
        "method": "POST",
        "url": base_url + "/instrument",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test instrument",
            "foldername": "test instrument",
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
                    "isassign": False,
                    "foldername": "",
                    "formconfig": ""
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
                "test instrument",
            ]
        }
    },
    {
        "name": "不带formconfig-名字为空",
        "method": "POST",
        "url": base_url + "/instrument",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "",
            "foldername": "test instrument",
        },
        "test": {
            "status_code": 200,
            "json_schema": {
                "data": "",
                "message": "新增失败",
                "success": False,
                "code": 2002
            },
            "attr": {
                "code": 2002,
                "success": False,
                "message": "新增失败"
            },
        }
    },
    {
        "name": "不带formconfig-路径为空",
        "method": "POST",
        "url": base_url + "/instrument",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test instrument",
            "foldername": "",
        },
        "test": {
            "status_code": 200,
            "json_schema": {
                "data": "",
                "message": "新增失败",
                "success": False,
                "code": 2002
            },
            "attr": {
                "code": 2002,
                "success": False,
                "message": "新增失败"
            },
        }
    },
    {
        "name": "带formconfig但为空",
        "method": "POST",
        "url": base_url + "/instrument",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "name": "test instrument",
            "foldername": "test instrument",
            "formconfig": ""
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
                    "isassign": False,
                    "foldername": "",
                    "formconfig": ""
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
                "test instrument",
            ]
        }
    },
]
