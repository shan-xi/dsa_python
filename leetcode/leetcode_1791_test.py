import unittest

from leetcode_1791 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.findCenter([[1, 2], [2, 3], [4, 2]])
        exp = 2
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]])
        exp = 1
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
