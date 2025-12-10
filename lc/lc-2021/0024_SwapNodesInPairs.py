# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Need two pointers to mark the current head node and the next head node
        """
        # create a dummy head
        dh = ListNode(next=head)
        curr = dh

        while curr.next and curr.next.next:
            tmp = curr.next
            # swap
            curr.next = tmp.next
            tmp.next = tmp.next.next
            curr.next.next = tmp

            # update curr
            curr = tmp
        return dh.next
