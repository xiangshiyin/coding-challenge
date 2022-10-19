#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set a dummy head
        dh = ListNode(next=head)
        p1 = p2 = dh
        # move p2 n steps forward
        step = 0
        while step < n:
            p2 = p2.next
            step += 1

        # move both pointers
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return dh.next


# @lc code=end
