# 1561. Maximum Number of Coins You Can Get
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        lp = 0
        rp = len(piles) - 1
        my_coins = 0
        while lp < rp:
            my_coins += piles[rp - 1]
            lp += 1
            rp -= 2
        return my_coins
