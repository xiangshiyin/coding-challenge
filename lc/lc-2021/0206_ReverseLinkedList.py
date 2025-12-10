# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         # exceptions
#         if not head or not head.next:
#             return head

#         # use a stack!
#         stack = []
#         h = head
#         while h:
#             stack.append(h)
#             h = h.next

#         # reverse the linked list
#         h2 = ListNode()
#         p2 = h2
#         while stack:
#             p2.next = stack.pop()
#             p2 = p2.next
#         p2.next = None

#         return h2.next


class Solution:
    """
    Simple iterative
    """

    def reverseList(self, head: ListNode) -> ListNode:
        # exceptions
        if not head or not head.next:
            return head
        # traverse the list
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


# solution as 11/16/2021
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         '''
#         no stack
#         '''
#         # exceptions
#         if not head or not head.next:
#             return head

#         pre = head
#         cur = head.next

#         while cur:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         head.next = None
#         return pre
