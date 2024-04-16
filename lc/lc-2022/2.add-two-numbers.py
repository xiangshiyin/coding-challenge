#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         carry = 0
#         head = l1
#         tail = None
#         while l1 and l2:
#             curr = l1.val + l2.val + carry
#             carry = curr // 10
#             left = curr % 10
#             l1.val = left
#             if not l1.next and l2.next:
#                 l1.next = l2.next
#                 l2.next = None
#             elif not l1.next and not l2.next:
#                 tail = l1
#             l1 = l1.next
#             l2 = l2.next

#         while l1:
#             curr = l1.val + carry
#             carry = curr // 10
#             left = curr % 10
#             l1.val = left
#             if not l1.next:
#                 tail = l1
#             l1 = l1.next

#         if carry:
#             tail.next = ListNode(val=carry)

#         return head


# solution on 2022-09-26
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carryover = 0
        p1 = l1
        p2 = l2
        while p1 and p2:
            temp = p1.val + p2.val + carryover
            p1.val = temp % 10
            carryover = temp // 10
            if not p1.next:
                if p2.next:  # reached the end
                    p1.next = p2.next
                elif carryover > 0:
                    p1.next = ListNode(val=0)
                p1 = p1.next
                break
            p1 = p1.next
            p2 = p2.next

        while p1:
            temp = p1.val + carryover
            p1.val = temp % 10
            carryover = temp // 10
            if not p1.next and carryover > 0:
                p1.next = ListNode(val=carryover)
                break
            p1 = p1.next
        return l1


# @lc code=end
