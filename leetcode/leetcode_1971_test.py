import unittest

from leetcode_1971 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2)
        exp = True
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
        exp = False
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
