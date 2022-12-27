# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if len(s) < 2 or numRows == 1:
#             return s
#
#         interval = numRows + (numRows - 2)
#         r = ""
#         for i, v in enumerate(s):
#             if i > numRows - 1:
#                 break
#
#             a = i
#             b = interval - i
#             if a == 0 or a == numRows - 1:
#                 while a < len(s):
#                     r += s[a]
#                     a += interval
#             else:
#                 while a < len(s) or b < len(s):
#                     if a < len(s):
#                         r += s[a]
#                     if b < len(s):
#                         r += s[b]
#                     a += interval
#                     b += interval
#         return r

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = []
        n = len(s)
        chars_in_section = 2 * (numRows - 1)

        for curr_row in range(numRows):
            index = curr_row
            while index < n:
                answer.append(s[index])

                # If curr_row is not the first or last row,
                # then we have to add one more character of current section.
                if curr_row != 0 and curr_row != numRows - 1:
                    chars_in_between = chars_in_section - 2 * curr_row
                    second_index = index + chars_in_between

                    if second_index < n:
                        answer.append(s[second_index])
                # Jump to same row's first character of next section.
                index += chars_in_section

        return "".join(answer)