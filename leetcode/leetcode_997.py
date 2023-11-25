# 997. Find the Town Judge
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = [0] * (n + 1)

        for a, b in trust:
            d[a] -= 1
            d[b] += 1

        for i in range(1, n + 1):
            if d[i] == n - 1:
                return i

        return -1
