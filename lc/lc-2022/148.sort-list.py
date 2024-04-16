#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        merge sort in linked list
        """
        # edge case
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # cut the list into 2 pieces
        start = slow.next  # start of 2nd half
        slow.next = None  # cut out the 1st half
        # sort them separately
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)

    def merge(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        if not l:
            return r
        if not r:
            return l

        p = dh = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        if r:
            p.next = r
        else:
            p.next = l

        return dh.next


# @lc code=end
