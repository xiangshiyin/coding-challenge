#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set((0, c) for c in range(n)) | set((r, 0) for r in range(m))
        atlantic = set((m - 1, c) for c in range(n)) | set((r, n - 1) for r in range(m))

        # find out all cells that connect to pacific or atlantic
        def bfs(starts, m, n):
            from collections import deque

            visited = [
                [1 if (r, c) in starts else 0 for c in range(n)] for r in range(m)
            ]
            drcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            ans = set(starts)

            q = deque(starts)
            while q:
                r, c = q.popleft()
                visited[r][c] = 1
                for dr, dc in drcs:
                    if (
                        0 <= r + dr < m
                        and 0 <= c + dc < n
                        and visited[r + dr][c + dc] == 0
                        and heights[r + dr][c + dc] >= heights[r][c]
                    ):
                        q.append((r + dr, c + dc))
                        visited[r + dr][c + dc] = 1
                        ans.add((r + dr, c + dc))
            return ans

        ans1 = bfs(pacific, m, n)
        ans2 = bfs(atlantic, m, n)
        ans = [list(a) for a in ans1.intersection(ans2)]
        return ans


# @lc code=end
