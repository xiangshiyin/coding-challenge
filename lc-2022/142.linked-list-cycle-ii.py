#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return None

#         fast = slow = head
#         step = 0
#         # find the 1st meet
#         while slow and fast:
#             if not slow.next or not fast.next:
#                 return None
#             slow = slow.next
#             fast = fast.next.next
#             step += 1
#             if fast==slow:
#                 break

#         if not slow or not fast:
#             return None

#         # find the 2nd meet
#         slow2 = head
#         step = 0
#         while slow and slow2 and slow2 != slow:
#             slow = slow.next
#             slow2 = slow2.next
#             step += 1
#         return slow


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = slow = head
        while fast:  # find the first meet
            if not fast.next:
                return None
            fast = fast.next.next  # 2 steps
            slow = slow.next  # 1 step
            if fast == slow:  # found the 1st meet
                break

        if not fast:
            return None

        slow2 = head
        slow = fast
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow


# @lc code=end

