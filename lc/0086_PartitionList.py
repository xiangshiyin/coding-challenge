# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
        1. traverse the list
        2. when a node is smaller than x, move it to the head
        '''
        # create a dummy head
        dh = ListNode(next=head)
        prev = dh
        last_small = dh
        curr = head
        
        while curr:
            if curr.val < x:
                prev.next = curr.next
                curr.next = last_small.next
                last_small.next = curr
                # update the pointers
                last_small = curr
            prev = curr
            curr = curr.next    
            
        
        return dh.next
        