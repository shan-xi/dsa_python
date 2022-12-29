class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10

        return x == rev or x == rev // 10

    # def isPalindrome(self, x: int) -> bool:
    #
    #     if x < 0:
    #         return False
    #
    #     stack = []
    #     while x > 0:
    #         stack.append(x % 10)
    #         x = x // 10
    #
    #     if len(stack) % 2 == 0:
    #         a = 0
    #         b = len(stack) - 1
    #         while a < b:
    #             if stack[a] != stack[b]:
    #                 return False
    #             a += 1
    #             b -= 1
    #     else:
    #         a = 0
    #         b = len(stack) - 1
    #         while a < b - 1:
    #             if stack[a] != stack[b]:
    #                 return False
    #             a += 1
    #             b -= 1
    #
    #     return True
