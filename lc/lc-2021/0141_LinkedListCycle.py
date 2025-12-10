# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            p1 = head
            if head.next:
                p2 = head.next
            else:
                return False

            while p1 and p2:
                if p1 == p2:
                    return True
                if p1.next and p2.next and p2.next.next:
                    p1 = p1.next
                    p2 = p2.next.next
                else:
                    return False
        else:
            return False
