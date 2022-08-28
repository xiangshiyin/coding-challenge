#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        cur = head
        next = head.next
        while cur:
            cur.next = prev
            if not next:
                return cur
            prev = cur
            cur = next
            next = cur.next

        
# @lc code=end

