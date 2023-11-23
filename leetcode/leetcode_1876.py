# 1876. Substrings of Size Three with Distinct Characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i, c in enumerate(s):
            if i + 2 > len(s) - 1:
                break
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                count += 1
        return count
