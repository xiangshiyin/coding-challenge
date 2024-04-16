class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        BFS search
        '''
        
        # step 1: convert the deadends to a hash set
        dends = set(deadends)
        
        # step 2: bfs traversal, try to avoid dends
        lock = [0, 0, 0, 0, 0]
        visited = set()
        
        from collections import deque
        q = deque([lock])
        
        def nextsteps(i, j, k, l):
            return [
                [(i+1)%10, j, k, l],
                [(i+9)%10, j, k, l],
                [i, (j+1)%10, k, l],
                [i, (j+9)%10, k, l],
                [i, j, (k+1)%10, l],
                [i, j, (k+9)%10, l],
                [i, j, k, (l+1)%10],
                [i, j, k, (l+9)%10]
            ]
        
        while q:
            # pop
            i, j, k, l, step = q.popleft()
            # evaluate
            if f'{i}{j}{k}{l}' in dends:
                continue
            if f'{i}{j}{k}{l}' == target:
                return step
            
            # add children
            for m, n, o, p in nextsteps(i, j, k, l):
                if (m,n,o,p) not in dends and (m,n,o,p) not in visited:
                    q.append([m,n,o,p,step+1])
                    visited.add((m,n,o,p))
        return -1
        
            
            
        
        