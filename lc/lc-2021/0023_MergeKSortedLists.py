# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         '''
#         Use the sorted function, O(nlogn)
#         '''
#         head = ListNode(0)
#         p = head

#         nodes = []
#         # concatenate all list values
#         for l in lists:
#             while l:
#                 nodes.append(l)
#                 l = l.next

#         # sort nodes
#         nodes = sorted(nodes, key=lambda x: x.val)

#         # generate the output
#         for node in nodes:
#             p.next = node
#             p = node
#         p.next = None

#         return head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        compare one by one, with heap
        """
        from heapq import heapify, heappush, heappop

        head = ListNode(0)  # dummy head
        hp = head

        # sort the head from each linked list
        tmp = [
            (node.val, id(node), node)
            for node in lists
            if node != None and node.val != None
        ]
        # create min heap
        heapify(tmp)

        while tmp:
            # pop out the smallest
            smallest = heappop(tmp)[2]
            if smallest.next:
                heappush(
                    tmp, (smallest.next.val, id(smallest.next), smallest.next)
                )  # add next node
            # update hp
            hp.next = smallest
            hp = hp.next
        hp.next = None

        return head.next
