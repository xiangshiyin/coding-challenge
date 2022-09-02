#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[0] * n for r in range(m)]

        def dfs(image, sr, sc, color):
            m = len(image)
            n = len(image[0])
            drc = [[0, -1], [-1, 0], [0, 1], [1, 0]]
            # color the target
            old_color = image[sr][sc]
            image[sr][sc] = color
            visited[sr][sc] = 1

            # flood the neighbors
            for dr, dc in drc:
                if (
                    0 <= sr + dr < m
                    and 0 <= sc + dc < n
                    and image[sr + dr][sc + dc] == old_color
                    and visited[sr + dr][sc + dc] == 0
                ):
                    dfs(image, sr + dr, sc + dc, color)

        dfs(image, sr, sc, color)
        return image


# @lc code=end

