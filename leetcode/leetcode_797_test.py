import unittest

from leetcode_797 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.allPathsSourceTarget([[1, 2], [3], [3], []])
        exp = [[0, 1, 3], [0, 2, 3]]
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []])
        exp = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
