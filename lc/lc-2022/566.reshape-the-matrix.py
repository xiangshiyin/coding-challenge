#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # check if reshape is possible
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        # reshape
        output = [[0] * c for i in range(r)]  # placeholder
        for i in range(m):
            for j in range(n):
                idx = n * i + j
                output[idx // c][idx % c] = mat[i][j]
        return output


# @lc code=end
