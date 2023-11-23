import unittest

from leetcode_1876 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.countGoodSubstrings("xyzzaz")
        exp = 1
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.countGoodSubstrings("aababcabc")
        exp = 4
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
