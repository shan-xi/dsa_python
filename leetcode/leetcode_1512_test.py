import unittest

from leetcode_1512 import Solution


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        ans = s.numIdenticalPairs([1, 2, 3, 1, 1, 3])
        exp = 4
        self.assertEqual(ans, exp)

    def test_case2(self):
        s = Solution()
        ans = s.numIdenticalPairs([1, 1, 1, 1])
        exp = 6
        self.assertEqual(ans, exp)

    def test_case3(self):
        s = Solution()
        ans = s.numIdenticalPairs([1, 2, 3])
        exp = 0
        self.assertEqual(ans, exp)


if __name__ == '__main__':
    unittest.main()
