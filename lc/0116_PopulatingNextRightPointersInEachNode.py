"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        bfs traversal the list level by level
        '''
        from collections import deque
        q = deque()
        if not root:
            return root
        
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                # add pointer
                if i < n - 1:
                    node.next = q[0]
                
                # add children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # print(n, len(q), [nd.val for nd in q])
        
        return root
    
    