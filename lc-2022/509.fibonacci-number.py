#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        minus_2 = 0
        minus_1 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1

        for i in range(2, n + 1):
            tmp = minus_1
            minus_1 = minus_1 + minus_2
            minus_2 = tmp
        return minus_1


# @lc code=end

