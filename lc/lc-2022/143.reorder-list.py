#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # find the middle point
        fast = slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None

        # reverse the 2nd half
        second = self.reverse(second)

        # merge the two halves
        while first and second:
            temp = second.next
            second.next = first.next
            first.next = second
            # update first and second
            first = second.next
            second = temp

    def reverse(self, head: Optional[ListNode]) -> None:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


# @lc code=end
