#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dh = ListNode(next=head)
        l = dh
        r = head
        while r and r.next:
            counter = 0
            while r and r.next and r.val == r.next.val:
                r = r.next
                counter += 1
            if counter == 0:
                l = r
                r = r.next
            else:
                if not r.next:
                    l.next = None
                    return dh.next
                else:
                    l.next = r.next
                    r = r.next
        return dh.next


# @lc code=end
