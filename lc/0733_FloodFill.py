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
        
        