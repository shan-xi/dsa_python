# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            c += n & 1
            n >>= 1
        return c
