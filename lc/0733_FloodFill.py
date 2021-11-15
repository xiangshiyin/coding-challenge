class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        visited = set()
        q = deque()
        q.append((sr, sc))
        
        while q:
            r, c = q.popleft()
            oldColor = image[r][c]
            image[r][c] = newColor
            
            # append neighbors
            for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                if (r+dr,c+dc) not in visited and 0<=r+dr<len(image) and 0<=c+dc<len(image[0]) and image[r+dr][c+dc]==oldColor:
                    q.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
        return image
        
# as of 11/14/2021
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         m = len(image)
#         n = len(image[0])
#         oldColor = image[sr][sc]
        
#         drcs = [
#             [0,1],
#             [0,-1],
#             [1,0],
#             [-1,0]
#         ]
#         seen = set()
#         from collections import deque
#         q = deque([(sr, sc)])
#         while q:
#             poi = q.popleft()
#             image[poi[0]][poi[1]] = newColor
            
#             for dr, dc in drcs:
#                 if 0 <= poi[0] + dr < m and 0 <= poi[1] + dc < n and (poi[0] + dr, poi[1] + dc) not in seen and image[poi[0] + dr][poi[1] + dc] ==oldColor:
#                     q.append((poi[0] + dr, poi[1] + dc))
#                     seen.add((poi[0] + dr, poi[1] + dc))
        
#         return image
                    
        
        
