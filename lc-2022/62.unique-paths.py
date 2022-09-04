#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or (i == 1 and j == 0):  # first row
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
        return grid[m - 1][n - 1]


# @lc code=end

