from config import *

folder = "新建节点配置"

request = [
    {
        "name": "正常",
        "method": "POST",
        "url": base_url + "/formbuilder",
        "header": {"Content-Type": "application/json", "username": "{{user}}", "usertoken": "{{token}}"},
        "body": {
            "project": {
                "objectId": "{{new_project}}"
            },
            "instrument": {
                "objectId": "{{new_instrument}}"
            },
            "user": {
                "objectId": "{{user}}"
            },
            "nodesconfig": str({"level": [
                {"component": "textArea", "editable": True, "index": 0, "label": "笔记", "description": "",
                 "placeholder": "请输入...", "options": [], "options2": [], "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:415"}], "level0": [
                {"component": "textArea", "editable": True, "index": 0, "label": "笔记", "description": "",
                 "placeholder": "请输入...", "options": [], "options2": [], "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:415"},
                {"component": "cascapeselect", "editable": True, "index": 1, "label": "样品尺寸", "description": "μm",
                 "placeholder": "请输入值...", "options": ["立方体", "柱体", "球体"],
                 "options2": {"选项一": ["选项一11", "选项二11"], "选项二": ["选项一22", "选项二22"], "null": [], "立方体": ["长", "宽", "高"],
                              "柱体": ["直径", "高度"], "球体": ["半径"]}, "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:937", "isAdded": False, "dateSets": [
                    {"name": "立方体", "code": "立方体",
                     "children": [{"name": "长", "code": "长"}, {"name": "宽", "code": "宽"}, {"name": "高", "code": "高"}]},
                    {"name": "柱体", "code": "柱体",
                     "children": [{"name": "直径", "code": "直径"}, {"name": "高度", "code": "高度"}]},
                    {"name": "球体", "code": "球体", "children": [{"name": "半径", "code": "半径"}]}]}], "level1": [
                {"component": "textArea", "editable": True, "index": 0, "label": "笔记", "description": "",
                 "placeholder": "请输入...", "options": [], "options2": [], "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:415"}], "level2": [
                {"component": "textArea", "editable": True, "index": 0, "label": "笔记", "description": "",
                 "placeholder": "请输入...", "options": [], "options2": [], "options3": [], "required": False,
                 "validation": "/.*/", "$$hashKey": "object:415"}]})
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
                "{{user}}",
                "{{new_project}}",
                "{{new_instrument}}"
            ]
        },
        "save": {
            "no_json": {
                "data.objectId": "new_formbuilder"
            },
        }
    },
]
