class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        start = 0
        end = 0

        for i in range(0, len(s)):
            length1 = self.expandArouncCenter(s, i, i)
            length2 = self.expandArouncCenter(s, i, i + 1)
            length = max(length1, length2)
            if length > end - start:
                start = i - int((length - 1) / 2)
                end = i + int(length / 2)
        return ''.join(s[start:(end + 1)])

    def expandArouncCenter(self, s: str, left: int, right: int) -> int:
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1
