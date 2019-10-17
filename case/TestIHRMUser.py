import unittest
import requests

import app
from api.UserApi import UserLogin
import json
from parameterized import parameterized


def read_json():
    # 1.创建空列表接收数据
    data = []
    # 2.读取文件，将解析到的数据追加至 列表
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        for value in json.load(f).values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            # 组织成元组
            data.append((mobile, password, success, code, message))
    # 3.返回列表
    return data


class TestUser(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.user_obj = UserLogin()

    def tearDown(self):
        self.session.close()

    def test_login_success(self):
        # 请求业务
        response = self.user_obj.login(self.session, "13800000002", "123456")
        result = response.json()
        print(result)
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))
        # 提取token值
        token = result.get("data")
        print("提取到的token值：", token)
        app.TOKEN = token

    @parameterized.expand(read_json())
    def test_login(self, mobile, password, success, code, message):
        print("❀" * 100)
        print(mobile, password, success, code, message)
        # 请求业务
        response = self.user_obj.login(self.session, mobile, password)
        # 断言业务
        print(response.json())
        result = response.json()
        self.assertEqual(success, result.get("success"))
        self.assertEqual(code, result.get("code"))
        self.assertIn(message, result.get("message"))
