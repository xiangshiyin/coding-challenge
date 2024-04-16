# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         '''
#         dfs search, only beats 15% in time, 5% in memory
#         '''
#         m = len(matrix)
#         n = len(matrix[0])
#         visited = set()
        
#         def dfs(row, col):
#             if matrix[row][col] == target:
#                 return True
#             if row + 1 < m and (row + 1, col) not in visited:
#                 visited.add((row + 1, col))
#                 if dfs(row + 1, col):
#                     return True
#             if col + 1 < n and (row, col + 1) not in visited:
#                 visited.add((row, col + 1))
#                 if dfs(row, col + 1):
#                     return True
#             return False
    
#         return dfs(0,0)
        
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         '''
#         binary search in each row
#         '''
#         m = len(matrix)
#         n = len(matrix[0])            
        
#         def binary_search(row, target):
#             lo = 0
#             hi = n - 1
#             while hi >= lo:
#                 mid = (lo + hi) // 2
#                 if matrix[row][mid] < target:
#                     lo = mid + 1
#                 elif matrix[row][mid] > target:
#                     hi = mid - 1
#                 else:
#                     return True
                
#         for i in range(m):
#             if binary_search(i, target):
#                 return True
        
#         return False
    

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         '''
#         optimized binary search, actually not faster than row based binary search
#         '''
#         m = len(matrix)
#         n = len(matrix[0])            
        
#         def binary_search(start, target, vertical):
#             lo = start
#             hi = n - 1 if vertical else m - 1
            
#             while hi >= lo:
#                 mid = (lo + hi) // 2
#                 if vertical:
#                     if matrix[start][mid] < target:
#                         lo = mid + 1
#                     elif matrix[start][mid] > target:
#                         hi = mid - 1
#                     else:
#                         return True
#                 else:
#                     if matrix[mid][start] < target:
#                         lo = mid + 1
#                     elif matrix[mid][start] > target:
#                         hi = mid - 1
#                     else:
#                         return True
#             return False
                
#         for i in range(min(m, n)):
#             if binary_search(i, target, True):
#                 return True
#             if binary_search(i, target, False):
#                 return True
        
#         return False
    

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         '''
#         binary search, divide and conquer
#         '''
#         m = len(matrix)
#         n = len(matrix[0])    
        
#         def search(left, right, up, down):
#             if left > right or up > down:
#                 return False
#             elif matrix[up][left] > target or matrix[down][right] < target:
#                 return False
            
#             row = up
#             mid = (left + right) // 2
#             # print(left, right, up, down, mid, matrix[row][mid] == target)
#             while row <= down and matrix[row][mid] <= target:
#                 if matrix[row][mid] == target:
#                     # print(True)
#                     return True
#                 row += 1
            
#             return search(left, mid - 1, up, down) or search(mid + 1, right, up, row - 1)
        
#         return search(0, n - 1, 0, m - 1)
    
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        binary search, divide and conquer
        '''
        m = len(matrix)
        n = len(matrix[0])    
        
        row = m - 1
        col = 0
        
        while col < n and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
            
        return False
    
        
            
            

