# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     '''
#     O(n) in space
#     '''
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         # build a hash table for list A
#         a = set()
#         while headA:
#             a.add(headA)
#             headA = headA.next

#         # traverse list B
#         while headB:
#             if headB in a:
#                 return headB
#             headB = headB.next

#         return None

# class Solution:
#     '''
#     O(1) in space
#     '''
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         # get the length of both lists
#         ha = headA
#         hb = headB

#         la = 0
#         while ha:
#             la += 1
#             ha = ha.next

#         lb = 0
#         while hb:
#             lb += 1
#             hb = hb.next

#         # set the start pointer on the longer list
#         hl = headA if la > lb else headB
#         hs = headB if la > lb else headA

#         il = 0
#         while il < abs(la - lb):
#             il += 1
#             hl = hl.next

#         # traverse both lists
#         while hl and hs and hl != hs:
#             hl = hl.next
#             hs = hs.next
#         if hl == hs:
#             return hl
#         else:
#             return None


class Solution:
    """
    smarter O(1) in space
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha = headA
        hb = headB

        while ha != hb:
            if ha:
                ha = ha.next
            else:
                ha = headB

            if hb:
                hb = hb.next
            else:
                hb = headA
        return ha
