# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # exceptions
        if head==None or head.next==None:
            return head
        
        # traverse the linked list
        left = head
        right = head.next
        
        while right:
            while right.val==left.val:
                right = right.next
                if right==None:
                    break
            if right:
                left.next = right
                left = right
                right = right.next
            else:
                left.next = None
                break
        return head
                
                