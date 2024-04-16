#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head or not head.next:
            return head

        # 2 pointers
        oh = odd = head
        eh = even = head.next
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = eh

        return oh


# @lc code=end
