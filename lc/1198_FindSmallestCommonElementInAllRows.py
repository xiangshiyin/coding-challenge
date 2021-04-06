# class Solution:
#     def smallestCommonElement(self, mat: List[List[int]]) -> int:
#         m = len(mat)
#         common = set(mat[0])
#         for i in range(1,m):
#             curr = set(mat[i])
#             common = common & curr
#         if len(common) > 0:
#             return sorted(common)[0]
#         else:
#             return -1


# class Solution:
#     def smallestCommonElement(self, mat: List[List[int]]) -> int:
#         m = len(mat)
#         n = len(mat[0])
#         tb = [0 for i in range(10000)]
#         for j in range(n):
#             for i in range(m):
#                 if (j > 0 and mat[i][j] != mat[i][j-1]) or (j == 0):
#                     tb[mat[i][j]] += 1
#                 if tb[mat[i][j]] == m:
#                     return mat[i][j]
#         return -1


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        pos = [0 for i in range(m)]
        cur_max = 0
        cnt = 0
        
        while True:
            for i in range(m):
                while pos[i] < n and mat[i][pos[i]] < cur_max:
                    pos[i] += 1
                
                if pos[i] >= n:
                    return -1
                
                if mat[i][pos[i]] != cur_max:
                    cur_max = mat[i][pos[i]]
                    cnt = 1
                else:
                    if pos[i] == 0 or (pos[i] > 0 and mat[i][pos[i]] != mat[i][pos[i] - 1]):
                        cnt += 1
                    if cnt == m:
                        return cur_max
                # print(cur_max)
        
        
        