#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        di = 0
        matrix = [[0] * n for i in range(n)]
        r = c = 0
        curr = 1
        while curr <= n**2:
            matrix[r][c] = curr
            trials = 0
            while (
                not (
                    0 <= r + drc[di][0] < n
                    and 0 <= c + drc[di][1] < n
                    and matrix[r + drc[di][0]][c + drc[di][1]] == 0
                )
                and trials < 4
            ):
                trials += 1
                di = (di + 1) % 4

            if (
                not (0 <= r + drc[di][0] < n and 0 <= c + drc[di][1] < n)
                or matrix[r + drc[di][0]][c + drc[di][1]] > 0
            ):
                break

            r += drc[di][0]
            c += drc[di][1]
            curr += 1

        return matrix


# @lc code=end
