#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#         # binary search across rows
#         u = 0
#         d = m - 1
#         while u <= d:
#             mid = (u + d) // 2
#             if matrix[mid][0] == target:
#                 return True
#             if matrix[mid][0] > target:
#                 if mid == 0:
#                     return False
#                 d = mid - 1
#             else:
#                 if mid + 1 < m and matrix[mid + 1][0] > target:
#                     break
#                 else:
#                     u = mid + 1

#         # binary search across cols
#         l = 0
#         r = n - 1
#         while l <= r:
#             mid2 = (l + r) // 2
#             if matrix[mid][mid2] == target:
#                 return True
#             if matrix[mid][mid2] > target:
#                 r = mid2 - 1
#             else:
#                 l = mid2 + 1
#         return False


# solution on 2022-10-24
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


# @lc code=end
