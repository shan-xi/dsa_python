import unittest

from longest_palidromic_substring import Solution


class TestLongestPalindromicSubstring(unittest.TestCase):

    def test_case1_success(self):
        actual = Solution().longestPalindrome(s="babad")
        expected1 = "bab"
        expected2 = "aba"
        self.assertTrue(actual == expected1 or actual == expected2)

    def test_case2_success(self):
        actual = Solution().longestPalindrome(s="cbbd")
        expected1 = "bb"
        self.assertEqual(expected1, actual)

    def test_case3_success(self):
        actual = Solution().longestPalindrome(s="abaceudekq")
        expected1 = "aba"
        self.assertTrue(actual == expected1)

    def test_case4_success(self):
        actual = Solution().longestPalindrome(s="ababab")
        expected1 = "ababa"
        expected2 = "babab"
        self.assertTrue(actual == expected1 or actual == expected2)

    def test_case5_success(self):
        actual = Solution().longestPalindrome(s="ceudekqaba")
        expected1 = "aba"
        self.assertTrue(actual == expected1)

    def test_case6_success(self):
        actual = Solution().longestPalindrome(s="a")
        expected1 = "a"
        self.assertTrue(actual == expected1)

    def test_case7_success(self):
        actual = Solution().longestPalindrome(s="ab")
        expected1 = "a"
        expected2 = "b"
        self.assertTrue(actual == expected1 or actual == expected2)

    def test_case8_success(self):
        actual = Solution().longestPalindrome(s="ac")
        expected1 = "a"
        expected2 = "c"
        self.assertTrue(actual == expected1 or actual == expected2)

    def test_case9_success(self):
        actual = Solution().longestPalindrome(s="aacabdkacaa")
        expected1 = "aca"
        self.assertTrue(actual == expected1)

    def test_case10_success(self):
        actual = Solution().longestPalindrome(s="ccc")
        expected1 = "ccc"
        self.assertTrue(actual == expected1)

    def test_case12_success(self):
        actual = Solution().longestPalindrome(s="tattarrattat")
        expected1 = "tattarrattat"
        self.assertTrue(actual == expected1)
