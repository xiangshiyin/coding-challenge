#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # ways(n) = ways(n - 1) + ways(n - 2)
        n2 = 1
        n1 = 1
        output = 1
        for i in range(2, n + 1):
            output = n1 + n2
            n2 = n1
            n1 = output
        return output


# @lc code=end

