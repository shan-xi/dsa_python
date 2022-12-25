class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128
        left = 0
        right = 0
        res = 0
        while right < len(s):
            c = s[right]
            index = chars[ord(c)]
            if index is not None and left <= index < right:
                left = index + 1
            res = max(res, right - left + 1)
            chars[ord(c)] = right
            right += 1
        return res
