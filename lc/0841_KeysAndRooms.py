class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        BFS traversal
        '''
        from collections import deque
        q = deque()
        n = len(rooms)
        
        # exceptions
        if n == 1:
            return True
        
        # BFS traversal the "graph"
        q.append(rooms[0])
        visited = [1 if i == 0 else 0 for i in range(n)]
        
        while q:
            # pop
            parent = q.popleft()
            
            # add children
            for key in parent:
                if not visited[key]:
                    q.append(rooms[key])
                    visited[key] = 1
            
            # print(q, visited)
        return sum(visited) == n
    