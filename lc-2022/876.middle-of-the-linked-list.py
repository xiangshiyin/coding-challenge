#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set slow and fast pointers
        fast = slow = ListNode(next = head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow.next
        else:
            return slow
        
# @lc code=end

