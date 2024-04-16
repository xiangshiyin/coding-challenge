#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

#         from collections import deque

#         drcs = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])
#         m = len(matrix)
#         n = len(matrix[0])
#         visited = set()
#         r = 0
#         c = 0
#         output = []
#         while len(visited) < m * n:
#             visited.add((r, c))
#             output.append(matrix[r][c])
#             if len(visited) == m * n:
#                 break
#             while (
#                 r + drcs[0][0] < 0
#                 or r + drcs[0][0] >= m
#                 or c + drcs[0][1] < 0
#                 or c + drcs[0][1] >= n
#                 or (r + drcs[0][0], c + drcs[0][1]) in visited
#             ):
#                 drcs.append(drcs.popleft())
#             r += drcs[0][0]
#             c += drcs[0][1]

#         return output


# solution on 2022-10-16
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        upper_bound = 0
        lower_bound = m - 1
        left_bound = 0
        right_bound = n - 1
        res = []

        while len(res) < m * n:
            if upper_bound <= lower_bound:
                for i in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][i])
                upper_bound += 1
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res.append(matrix[i][right_bound])
                right_bound -= 1
            if upper_bound <= lower_bound:
                for i in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[lower_bound][i])
                lower_bound -= 1
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    res.append(matrix[i][left_bound])
                left_bound += 1
        return res


# @lc code=end
