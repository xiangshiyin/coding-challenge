#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        from collections import deque

        q = deque()
        oranges = 0
        # collect all rotten orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    oranges += 1
                    if grid[i][j] == 2:
                        q.append((i, j, 0))

        counter = len(q)
        # exceptions
        if counter == 0:
            if oranges == 0:
                return 0
            else:
                return -1
        if counter == oranges:
            return 0

        drcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = 0
        while q:
            r, c, minute = q.popleft()
            ans = max(ans, minute)
            for dr, dc in drcs:
                if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == 1:
                    q.append((r + dr, c + dc, minute + 1))
                    grid[r + dr][c + dc] = 2
                    counter += 1
        if counter == oranges:
            return ans
        else:
            return -1


# @lc code=end
