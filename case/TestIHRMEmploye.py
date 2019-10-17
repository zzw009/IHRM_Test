import unittest
import requests

from api.EmpApi import EmpCRUD


class TestEmploye(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    def tearDown(self):
        self.session.close()

    def test_add_emp(self):
        response = self.emp_obj.add(self.session, "aaa0322351", "15689468523", "16419841")
        print("添加成功响应：", response.json())

    def test_update_emp(self):
        response = self.emp_obj.update(self.session, "1184388072665862144", "渣倩傻子")
        print("修改成功响应：", response.json())
        self.assertEqual(True, response.json().get("success"))

    def test_get_emp(self):
        response = self.emp_obj.get(self.session,"1184388072665862144")
        print("查看成功响应：", response.json())
        self.assertEqual(True, response.json().get("success"))

    def test_delete_emp(self):
        response = self.emp_obj.delete(self.session,"1184388072665862144")
        print("删除成功响应：", response.json())
        self.assertEqual(True, response.json().get("success"))
