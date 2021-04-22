# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        ## pop out
        counter = 0
        out = None
        while counter < n - 1:
            out = stack.pop()
            counter += 1
        
        node2del = stack.pop()
        
        if not stack:
            if out == None:
                head = None
            else:
                head = out
        else:
            stack[-1].next = out
        
        return head
    