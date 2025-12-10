"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        mapping = {node: Node(node.val, [])}

        q = [node]

        while q:
            n = q.pop()

            # add children
            for neighbor in n.neighbors:
                if neighbor not in mapping:
                    q.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val, [])
                mapping[n].neighbors.append(mapping[neighbor])

        return mapping[node]
