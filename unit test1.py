import unittest
from testprogram import program1

class My_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(program1.add_two_num(10,20),30)
    def test_two(self):
        self.assertEqual(program1.add_two_num(-100,100),0)

    def test_three(self):
        self.assertEqual(program1.add_two_num(-10,-20),-30)
    def test_four(self):
        self.assertEqual(program1.add_two_num(-40,3),-37)