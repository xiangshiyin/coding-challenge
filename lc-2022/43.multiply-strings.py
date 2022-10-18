#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         prod = [0] * (len(num1) + len(num2))
#         p = len(prod) - 1

#         for n1 in reversed(num1):
#             p2 = p
#             for n2 in reversed(num2):
#                 currProd = int(n1) * int(n2) + prod[p2]
#                 prod[p2] = currProd % 10
#                 prod[p2 - 1] += currProd // 10
#                 p2 -= 1
#             p -= 1

#         p3 = 0
#         while p3 < len(prod) - 1 and prod[p3] == 0:
#             p3 += 1

#         return "".join([str(digit) for digit in prod[p3:]])


# solution on 2022-10-18
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prod = [0] * (len(num1) + len(num2))
        p = len(prod) - 1

        for n2 in reversed(num2):
            p2 = p
            for n1 in reversed(num1):
                currProd = int(n2) * int(n1) + prod[p2]
                prod[p2] = currProd % 10
                prod[p2 - 1] += currProd // 10
                p2 -= 1
            p -= 1

        p3 = 0
        while p3 < len(prod) - 1 and prod[p3] == 0:
            p3 += 1

        return "".join([str(d) for d in prod[p3:]])


# @lc code=end
