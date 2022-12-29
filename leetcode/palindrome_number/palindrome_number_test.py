import unittest

from palindrome_number import Solution


class SolutionTest(unittest.TestCase):
    def test_isPalindrome_case1_success(self):
        got = Solution().isPalindrome(121)
        want = True
        self.assertEqual(got, want)

    def test_isPalindrome_case2_success(self):
        got = Solution().isPalindrome(-121)
        want = False
        self.assertEqual(got, want)

    def test_isPalindrome_case3_success(self):
        got = Solution().isPalindrome(10)
        want = False
        self.assertEqual(got, want)
