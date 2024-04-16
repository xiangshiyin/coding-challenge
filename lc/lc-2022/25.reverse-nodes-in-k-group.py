#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        temp = dh = ListNode()

        def evaluateLen(curr, k):
            node = curr
            counter = 0
            while node and counter < k - 1:
                node = node.next
                counter += 1
            return True if counter == k - 1 and node else False

        def reverse(curr, k):
            prev = None
            counter = k
            newTail = curr
            while curr and counter > 0:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                counter -= 1
            return prev, newTail, curr

        while curr:
            if evaluateLen(curr, k):
                prev, newTail, curr = reverse(curr, k)
                temp.next = prev
                temp = newTail
            else:
                break
        temp.next = curr

        return dh.next


# @lc code=end
