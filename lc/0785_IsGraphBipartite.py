class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        bfs traversal
        '''
        from collections import deque
        visited = {0:0}
        
        for i in range(len(graph)):
            if i in visited:
                queue = deque([(i,visited[i])])
            else:
                queue = deque([(i,0)])

            while queue:
                # pop
                node, color = queue.popleft()

                # add children
                if len(graph[node]) > 0:
                    for child in graph[node]:
                        if child not in visited:
                            queue.append((child, 1-color))
                            visited[child] = 1-color
                        elif child in visited and visited[child] != 1-color:
                            return False
        
        return True
            
            
            