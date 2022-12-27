import unittest

from tree_constructor import TreeConstructor


class TreeConstructorTest(unittest.TestCase):
    def test_testcase1_success(self):
        got = TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"])
        want = True
        self.assertEqual(got, want)

    def test_testcase2_success(self):
        got = TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"])
        want = False
        self.assertEqual(got, want)


    def test_testcase3_success(self):
        got = TreeConstructor(["(2,5)", "(2,6)"])
        want = False
        self.assertEqual(got, want)
