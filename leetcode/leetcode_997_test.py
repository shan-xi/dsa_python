import unittest

from leetcode_997 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.findJudge(2, [[1, 2]])
        exp = 2
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.findJudge(3, [[1, 3], [2, 3]])
        exp = 3
        self.assertEqual(ans, exp)

    def test_case3(self):
        s = Solution()
        ans = s.findJudge(3, [[1, 3], [2, 3], [3, 1]])
        exp = -1
        self.assertEqual(ans, exp)

    def test_case4(self):
        s = Solution()
        ans = s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
        exp = 3
        self.assertEqual(ans, exp)

    def test_case5(self):
        s = Solution()
        ans = s.findJudge(3, [[1, 2], [2, 3]])
        exp = -1
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
