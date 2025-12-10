# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapNodes(self, head: ListNode, k: int) -> ListNode:
#         # traverse the list, create a hash table
#         tb = {}
#         counter = 0
#         h = head
#         while h:
#             counter += 1
#             tb[counter] = h
#             h = h.next

#         # swap values
#         kb = tb[k] # kth node from the beginning
#         ke = tb[counter - k + 1] # kth node from the end
#         tmp = kb.val
#         kb.val = ke.val
#         ke.val = tmp

#         return head


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        2 pass, no hash table
        """
        # 1st pass, get the length and the the kth node from the beginning
        n = 0  # count the index
        h = head
        while h:
            n += 1
            if n == k:
                kb = h
            h = h.next

        # 2nd pass, get the kth node from the end
        counter = 0
        h = head
        while h:
            counter += 1
            if counter == n - k + 1:
                ke = h
                break
            h = h.next

        # swap the values
        tmp = kb.val
        kb.val = ke.val
        ke.val = tmp

        return head
