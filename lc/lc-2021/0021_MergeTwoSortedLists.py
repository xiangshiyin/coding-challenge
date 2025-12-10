# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #         # handle the exceptions
    #         if l1==None:
    #             return l2
    #         if l2==None:
    #             return l1

    #         # create pointers for l1 and l2
    #         n1 = l1
    #         n2 = l2

    #         # create a new linked list
    #         if n1.val<=n2.val:
    #             output_tail = n1
    #             n1 = n1.next
    #         else:
    #             output_tail = n2
    #             n2 = n2.next
    #         # locate the head of the new linked list
    #         output_head = output_tail

    #         while n1!=None and n2!=None:
    #             if n1.val <= n2.val:
    #                 output_tail.next = n1
    #                 n1 = n1.next
    #             else:
    #                 output_tail.next = n2
    #                 n2 = n2.next
    #             output_tail = output_tail.next
    #         if n1:
    #             while n1:
    #                 output_tail.next = n1
    #                 n1 = n1.next
    #                 output_tail = output_tail.next

    #         if n2:
    #             while n2:
    #                 output_tail.next = n2
    #                 n2 = n2.next
    #                 output_tail = output_tail.next

    #         return output_head

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2

        return prehead.next


# solution as of 11/16/2021, redudant pointers (p1,p2)
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # exceptions
#         if not l1:
#             return l2
#         if not l2:
#             return l1

#         p1 = l1
#         p2 = l2
#         dh = ListNode()
#         pdh = dh

#         while p1 and p2:
#             if p1.val <= p2.val:
#                 pdh.next = p1
#                 p1 = p1.next
#             else:
#                 pdh.next = p2
#                 p2 = p2.next

#             pdh = pdh.next

#         if p1:
#             pdh.next = p1
#         else:
#             pdh.next = p2

#         return dh.next
