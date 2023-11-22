import unittest

from leetcode_228 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.countBits(2)
        exp = [0, 1, 1]
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.countBits(5)
        exp = [0, 1, 1, 2, 1, 2]
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
