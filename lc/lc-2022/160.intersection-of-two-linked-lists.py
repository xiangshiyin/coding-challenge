#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        ha = headA
        hb = headB
        while ha != hb:
            if ha:
                ha = ha.next
            else:
                ha = headB
            if hb:
                hb = hb.next
            else:
                hb = headA
        return ha


# @lc code=end
