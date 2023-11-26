import unittest

from leetcode_1561 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.maxCoins([2, 4, 1, 2, 7, 8])
        exp = 9
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.maxCoins([2, 4, 5])
        exp = 4
        self.assertEqual(ans, exp)

    def test_case3(self):
        s = Solution()
        ans = s.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4])
        exp = 18
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
