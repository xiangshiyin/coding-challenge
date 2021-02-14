"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        node = Node(head.val, None, None)
        self.visited[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node

# solution on 2/10/2021
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         '''
#         Use a hash table to record the node index
#         '''
#         head1 = head
#         head2 = Node(-1) # the cloned linked list
#         prev = head2
#         nodes = []
#         pos = {}
#         idx = 0
        
#         # 1st pass: copy the next nodes
#         while head:
#             # create a new node
#             curr = Node(head.val)
#             nodes.append(curr) # record the node in a list
#             pos[head] = idx # record the node position in the list
#             idx += 1
#             # connect to prev
#             prev.next = curr
#             # update pointer
#             prev = prev.next
#             head = head.next
  
#         # 2nd pass: connect the random pointers
#         head = head1
#         tmp = head2.next
#         while head:
#             # print(head.random)
#             if head.random:
#                 tmp.random = nodes[pos[head.random]]
#             head = head.next
#             tmp = tmp.next
        
#         return head2.next       
        