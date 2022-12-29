import unittest

from reverse_integer import Solution


class SolutionTest(unittest.TestCase):
    def test_reverse_case1_success(self):
        got = Solution().reverse(123)
        want = 321
        self.assertEqual(got, want)

    def test_reverse_case2_success(self):
        got = Solution().reverse(-123)
        want = -321
        self.assertEqual(got, want)

    def test_reverse_case3_success(self):
        got = Solution().reverse(120)
        want = 21
        self.assertEqual(got, want)

    def test_reverse_case4_success(self):
        got = Solution().reverse(1534236469)
        want = 0
        self.assertEqual(got, want)
