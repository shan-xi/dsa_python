# 338. Counting Bits
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        r = [0] * (n + 1)
        for i in range(1, n + 1):
            r[i] = r[i >> 1] + (i & 1)
        return r

        # m = {0: 0, 1: 1}
        # arr = []
        # for x in range(0, n + 1):
        #     if x in m:
        #         arr.append(m.get(x))
        #     else:
        #         n1 = x % 2
        #         n2 = int(x / 2)
        #         en = m.get(n2)
        #         v = n1 + en
        #         arr.append(v)
        #         m.update({x: v})
        # return arr
