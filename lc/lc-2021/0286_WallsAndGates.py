# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         BFS solution
#         """
#         m = len(rooms)
#         n = len(rooms[0])

#         # step 1: find all gates
#         gates = [[i,j] for i in range(m) for j in range(n) if rooms[i][j]==0]

#         # step 2: bfs traversal from every gate, update the distances
#         from collections import deque

#         for gate in gates:
#             q = deque([(gate[0], gate[1], 0)])
#             visited = set()
#             while q:
#                 x, y, dist = q.popleft()
#                 rooms[x][y] = min(dist, rooms[x][y])

#                 # add neighbors
#                 for x2, y2 in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
#                     if 0 <= x2 < m and 0 <= y2 < n and (x2,y2) not in visited and rooms[x2][y2] > 0:
#                         q.append((x2, y2, dist + 1))
#                         visited.add((x2,y2))


# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         BFS with much less memory
#         """
#         m = len(rooms)
#         n = len(rooms[0])

#         # step 1: bfs traversal from every gate, update the distances
#         from collections import deque

#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j] == 0:
#                     q = deque([(i, j, 0)])
#                     visited = set()
#                     while q:
#                         x, y, dist = q.popleft()
#                         rooms[x][y] = min(dist, rooms[x][y])

#                         # add neighbors
#                         for x2, y2 in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
#                             if 0 <= x2 < m and 0 <= y2 < n and (x2,y2) not in visited and rooms[x2][y2] > 0:
#                                 q.append((x2, y2, dist + 1))
#                                 visited.add((x2,y2))


# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         Modified BFS, faster in running time
#         """
#         m = len(rooms)
#         n = len(rooms[0])

#         # step 1: bfs traversal from every gate, update the distances
#         from collections import deque

#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j] == 0:
#                     q = deque([(i, j, 0)])
#                     visited = set()
#                     while q:
#                         x, y, dist = q.popleft()
#                         rooms[x][y] = dist

#                         # add neighbors
#                         for x2, y2 in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
#                             if 0 <= x2 < m and 0 <= y2 < n and rooms[x2][y2] > dist:
#                                 q.append((x2, y2, dist + 1))
#                                 visited.add((x2,y2))


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        DFS
        """

        def dfs(x, y, dist):
            if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] >= dist:
                rooms[x][y] = dist
                dfs(x, y + 1, dist + 1)
                dfs(x, y - 1, dist + 1)
                dfs(x + 1, y, dist + 1)
                dfs(x - 1, y, dist + 1)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
