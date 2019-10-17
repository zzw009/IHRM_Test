import unittest

from case.TestIHRMEmploye import TestEmploye
from case.TestIHRMUser import TestUser

suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success"))
suite.addTest(TestEmploye("test_add_emp"))
suite.addTest(TestEmploye("test_update_emp"))
suite.addTest(TestEmploye("test_get_emp"))
suite.addTest(TestEmploye("test_delete_emp"))

runner = unittest.TextTestRunner()
runner.run(suite)

