import unittest

import time

from case.TestIHRMEmploye import TestEmploye
from case.TestIHRMUser import TestUser
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))
suite.addTest(TestEmploye("test_add_emp"))
suite.addTest(TestEmploye("test_update_emp"))
suite.addTest(TestEmploye("test_get_emp"))
suite.addTest(TestEmploye("test_delete_emp"))

# 打开文件流
file_to = "./report/report.html" + time.strftime("%Y-%m-%d %H-%M-%S") + ".html"
with open(file_to, "wb") as f:
    # 使用 HTMLTestRunner 要运行测试套件，将结果写入文件流
    runner = HTMLTestRunner(f, title="测试报告", description="v1.0")
    runner.run(suite)
