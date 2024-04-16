class Solution:
    def numSquares(self, n: int) -> int:
        '''
        BFS search from 0
        '''
        from collections import deque
        q = deque([[0,0]])
        visited = set()
        
        while q:
            # pop
            num, step = q.popleft()
            # evalute
            if num == n:
                return step
            
            # add children
            for v in range(1,int((n-num)**0.5)+1):
                if num + v**2 not in visited:
                    q.append([num + v**2,step+1])
                    visited.add(num + v**2)
            # print(q)
        return -1
    
        