# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         '''
#         with extra memory space
#         '''
#         # create a dummy node
#         dh = ListNode(next=head)
#         n = dh
#         stack = []
        
#         while head:
#             if len(stack) < k:
#                 stack.append(head)
#                 head = head.next
#             if len(stack) == k:
#                 while stack:
#                     n.next = stack.pop()
#                     n = n.next
        
#         if not stack:
#             n.next = None
            
#         for node in stack:
#             n.next = node
#             n = n.next
        
#         return dh.next
            
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
        with no extra memory space
        '''
        if k == 1:
            return head
        
        # create a dummy head
        dh = ListNode()
        p = dh
        counter = 0
        
        while head:
            counter += 1
            if counter == 1:
                start = head
            
            head_next = head.next
            
            if counter == k:
                end = head
                # reverse the list
                prev = None
                curr = start
                while True:
                    nxt = curr.next
                    curr.next = prev
                    if curr == end:
                        break
                    prev = curr
                    curr = nxt
                p.next = end
                p = start
                counter = 0
            head = head_next
        
        if counter > 0:
            p.next = start
        
        return dh.next
        
                
        

