#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        grid = [0] * n
        for i in range(n):
            if i <= 1:
                grid[i] = 0
            else:
                grid[i] = min(grid[i - 2] + cost[i - 2], grid[i - 1] + cost[i - 1])
        return min(grid[n - 2] + cost[n - 2], grid[n - 1] + cost[n - 1])


# @lc code=end

