#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dh = ListNode(next=head)
        h = dh
        while h.next and h.next.next:
            first = h.next
            second = first.next
            h.next = second
            first.next = second.next
            second.next = first
            h = h.next.next

        return dh.next


# @lc code=end
