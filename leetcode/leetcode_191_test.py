import unittest

from leetcode_191 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.hammingWeight(0b00000000000000000000000000001011)
        exp = 3
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.hammingWeight(0b00000000000000000000000010000000)
        exp = 1
        self.assertEqual(ans, exp)

    def test_case3(self):
        s = Solution()
        ans = s.hammingWeight(0b11111111111111111111111111111101)
        exp = 31
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
