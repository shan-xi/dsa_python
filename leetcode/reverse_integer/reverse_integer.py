import math


class Solution:
    def reverse(self, x: int) -> int:
        # 123 % 10 = 3
        # 123 // 10 = 12
        # 1

        # 12 % 10 = 2
        # 12 // 10 = 1
        # 2

        # 1 % 10 = 1
        # 1 // 10 = 0
        # 3

        isNegtive = 1
        if x < 0:
            x = x * -1
            isNegtive = -1

        stack = []
        while x > 0:
            stack.append(x % 10)
            x = x // 10

        level = 0
        sum_value = 0
        if len(stack) == 0:
            return 0
        i = stack.pop()
        while i is not None:
            sum_value += i * math.pow(10, level)
            level += 1
            if len(stack) == 0:
                break
            i = stack.pop()

        r = int(sum_value) * isNegtive
        if r > math.pow(2, 31) - 1 or r < -1 * math.pow(2, 31):
            return 0
        else:
            return r
    # def reverse(self, x: int) -> int:
    #     is_negtive = 1
    #     if x < 0:
    #         x = x * -1
    #         is_negtive = -1
    #     rev = 0
    #     max_int32 = int(math.pow(2, 31)) - 1
    #     min_int32 = -int(math.pow(2, 31))
    #     while x != 0:
    #         pop = x % 10
    #         x = x // 10
    #
    #         if rev > max_int32 / 10 or (rev == max_int32 and pop > 7):
    #             return 0
    #         if rev < min_int32 / 10 or (rev == min_int32 and pop < -8):
    #             return 0
    #
    #         temp = rev * 10 + pop
    #         rev = temp
    #
    #     return rev * is_negtive
