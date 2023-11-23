from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = dict()
        c = 0
        for n in nums:
            if n not in h:
                h.update({n: 1})
            else:
                c += h.get(n)
                h.update({n: h.get(n) + 1})
        return c
