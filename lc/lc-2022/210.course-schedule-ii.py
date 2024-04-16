#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        self.hasCycle = False
        self.ans = []

        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[p].append(c)

        visited = [0 for i in range(numCourses)]
        on_path = [0 for i in range(numCourses)]

        def traverse(graph, node, visited):
            if on_path[node]:
                self.hasCycle = True
                return
            if visited[node]:
                return
            visited[node] = 1  # pre-order
            on_path[node] = 1
            for nxt in graph[node]:
                traverse(graph, nxt, visited)
            on_path[node] = 0
            self.ans.append(node)  # post-order

        for node in range(numCourses):
            traverse(graph, node, visited)
            if self.hasCycle:
                return []
        return self.ans[::-1]


# @lc code=end
