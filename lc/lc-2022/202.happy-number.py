#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit**2
                n = n // 10
            return sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next(n)
        if n == 1:
            return True
        else:
            return False


# @lc code=end
