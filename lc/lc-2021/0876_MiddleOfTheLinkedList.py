# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # 1. get the length of the linked list
#         h = ListNode(next=head)
#         n = 0
#         while h.next:
#             n += 1
#             h = h.next

#         # 2. find the middle node
#         counter = 0
#         h = ListNode(next=head)
#         while counter <= n // 2:
#             h = h.next
#             counter += 1
#         return h

# 2nd solution as of 11/12/2021
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        fast and slow pointers
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
