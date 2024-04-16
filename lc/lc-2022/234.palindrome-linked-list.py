#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the break point
        slow = fast = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if not slow.next:
            return True

        # reverse the 2nd half
        prev = None
        curr = slow.next
        while curr and curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev

        # compare 1st and 2nd halves
        p1 = head
        p2 = curr
        while p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next

        if p2:
            return False
        else:
            return True


# @lc code=end
