import unittest
from testprogram import program2

class my_search(unittest.TestCase):
    def test(self):
        self.assertEqual(program2.search(2),0)
    def test1(self):
        self.assertEqual(program2.search(4),1)

