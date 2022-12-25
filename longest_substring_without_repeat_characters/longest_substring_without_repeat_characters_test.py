import unittest

from longest_substring_without_repeat_characters import Solution

class TestLongestSubstringWithoutRepeatCharacters(unittest.TestCase):
    def test_case1_success(self):
        actual = Solution().lengthOfLongestSubstring(s="abcabcbb")
        expected = 3
        self.assertEqual(actual, expected)
    def test_case2_success(self):
        actual = Solution().lengthOfLongestSubstring(s="bbbbb")
        expected = 1
        self.assertEqual(actual, expected)
    def test_case3_success(self):
        actual = Solution().lengthOfLongestSubstring(s="pwwkew")
        expected = 3
        self.assertEqual(actual, expected)
    def test_case4_success(self):
        actual = Solution().lengthOfLongestSubstring(s="aab")
        expected = 2
        self.assertEqual(actual, expected)
    def test_case5_success(self):
        actual = Solution().lengthOfLongestSubstring(s="dvdf")
        expected = 3
        self.assertEqual(actual, expected)
    def test_case6_success(self):
        actual = Solution().lengthOfLongestSubstring(s="abba")
        expected = 2
        self.assertEqual(actual, expected)
    def test_case7_success(self):
        actual = Solution().lengthOfLongestSubstring(s=" ")
        expected = 1
        self.assertEqual(actual, expected)
