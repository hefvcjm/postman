from config import *

# 所属文件夹名称
folder = "登录"

# 测试请求集合
request = [
    {
        "name": "用户名登录",
        "method": "GET",
        "url": base_url + "/user/login?username=administrator&password=xA123456",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "查询成功"
            },
            "has": [
                "administrator"
            ]
        }
    },
    {
        "name": "用户名登录-密码错误",
        "method": "GET",
        "url": base_url + "/user/login?username=administrator&password=xA123446",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"message": "", "success": False, "code": 2020},
            "attr": {
                "code": 2020,
                "success": False,
                "message": "密码错误",
            },
        }
    },
    {
        "name": "用户名登录-不输入密码",
        "method": "GET",
        "url": base_url + "/user/login?username=administrator&password=",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"message": "", "success": False, "code": 2020},
            "attr": {
                "code": 2020,
                "success": False,
                "message": "密码错误",
            },
        }
    },
    {
        "name": "用户名登录-未注册用户",
        "method": "GET",
        "url": base_url + "/user/login?username=administ&password=fasdfa",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"message": "", "success": False, "code": 2020},
            "attr": {
                "code": 2019,
                "success": False,
                "message": "用户不存在",
            },
        }
    },
    {
        "name": "邮箱登录-正常",
        "method": "GET",
        "url": base_url + "/user/login?username=admin@mkapp.com&password=xA123456",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"data": {}, "message": "", "code": 0, "success": False},
            "attr": {
                "code": 0,
                "success": True,
                "message": "查询成功"
            },
            "has": [
                "admin@mkapp.com"
            ]
        }
    },
    {
        "name": "邮箱登录-密码错误",
        "method": "GET",
        "url": base_url + "/user/login?username=admin@mkapp.com&password=xA123446",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"message": "", "success": False, "code": 2020},
            "attr": {
                "code": 2020,
                "success": False,
                "message": "密码错误",
            },
        }
    },
    {
        "name": "邮箱登录-不输入密码",
        "method": "GET",
        "url": base_url + "/user/login?username=admin@mkapp.com&password=",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"message": "", "success": False, "code": 2020},
            "attr": {
                "code": 2020,
                "success": False,
                "message": "密码错误",
            },
        }
    },
    {
        "name": "邮箱登录-未注册用户",
        "method": "GET",
        "url": base_url + "/user/login?username=fdsafgds@mkapp.com&password=fasdfa",
        "header": {"Content-Type": "application/json"},
        "body": {},
        "test": {
            "status_code": 200,
            "json_schema": {"message": "", "success": False, "code": 2020},
            "attr": {
                "code": 2019,
                "success": False,
                "message": "用户不存在",
            },
        }
    },
]
