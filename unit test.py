import unittest
import HtmlTestRunner
class My_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(3+4,7)
    def test_demo(self):
        self.assertEqual(10+10,20)
test_suite=unittest.TestSuite()
test_suite.addTest(My_test("test1"))
testRunner=HtmlTestRunner.HTMLTestRunner(output='report')
testRunner.run(test_suite)