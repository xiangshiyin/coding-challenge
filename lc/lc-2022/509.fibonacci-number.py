#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
# class Solution:
#     def fib(self, n: int) -> int:
#         minus_2 = 0
#         minus_1 = 1
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1

#         for i in range(2, n + 1):
#             tmp = minus_1
#             minus_1 = minus_1 + minus_2
#             minus_2 = tmp
#         return minus_1


# solution on 2022-09-18
class Solution:
    from functools import lru_cache

    @lru_cache
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)


# @lc code=end
