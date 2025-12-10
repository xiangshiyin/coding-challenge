#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 1st pass, flip each row
        for i in range(n):
            l = 0
            r = n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1

        # 2nd pass, flip around the diagonal direction, base at (n-1,0)
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = (
                    matrix[n - 1 - j][n - 1 - i],
                    matrix[i][j],
                )


# @lc code=end
