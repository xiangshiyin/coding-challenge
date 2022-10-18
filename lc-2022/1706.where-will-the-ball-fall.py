#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#

# @lc code=start
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        a ball can move freely in vertical direction to the next level
        """
        m = len(grid)
        n = len(grid[0])
        res = []

        for i in range(n):  # n different starting points
            c = i
            for r in range(m):
                c2 = c + grid[r][c]
                if c2 < 0 or c2 >= n or grid[r][c2] != grid[r][c]:
                    res.append(-1)
                    break
                c = c2
            if len(res) < i + 1:
                res.append(c)
        return res


# @lc code=end
