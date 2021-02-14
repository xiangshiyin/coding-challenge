# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:25:16 2017

@author: xyin
"""

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.


# class ListNode(object):
#     def __init__(self, data):
#         self.val = data
#         self.next = None


# class LinkedList(object):
#     def __init__(self, head=None):
#         self.head = head
#         if self.head is None:
#             self.end = self.head
#         else:
#             current = self.head
#             found = False
#             while current is not None and found == False:
#                 if current.next is None:
#                     self.end = current
#                     found = True

#     def size(self):
#         current = self.head
#         counter = 0
#         while current is not None:
#             counter += 1
#             current = current.next
#         return(counter)

#     def insert(self, data):
#         new_node = ListNode(data)
#         new_node.next = self.head
#         self.head = new_node

#     def append(self, data):
#         new_node = ListNode(data)
#         self.end.next = new_node
#         self.end = new_node

#     def search(self, data):
#         current = self.head
#         found = False
#         while current is not None and found == False:
#             if current.val == data:
#                 found = True
#             else:
#                 current = current.next
#         if current is None:
#             raise ValueError("Data not in list")
#         return(current)


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if l1 == None and l2 == None:
#             return ListNode(None)
#         else:
#             if l1 == None:
#                 return l2
#             if l2 == None:
#                 return l1

#         node = ListNode(0)
#         nodex = node
#         left = l1
#         right = l2
#         while left != None or right != None:
#             sum = (left.val if left != None else 0) + \
#                 (right.val if right != None else 0) + nodex.val
#             nodex.val = sum if sum < 10 else sum % 10
#             nodex.next = ListNode(0) if sum < 10 else ListNode(1)
#             nodexx = nodex
#             print(sum, nodex.val, nodex.next)
#             left = left.next if left != None else None
#             right = right.next if right != None else None
#             nodex = nodex.next
#             if left == None and right == None and nodex.val == 0:
#                 nodexx.next = None
#         return(node)


# if __name__ == '__main__':
#     l1 = ListNode(2)
#     l1.next = ListNode(5)
#     l1.next.next = ListNode(1)
#     l1.next.next.next = ListNode(3)
#     l2 = ListNode(8)
#     l2.next = ListNode(1)
#     l2.next.next = ListNode(2)
#     l2.next.next.next = ListNode(4)
#     solve = Solution()
#     x = solve.addTwoNumbers(l1, l2)


# on 1/13/2020
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sumNodeHead = ListNode(0)
        sumNode = sumNodeHead
        
        while l1 and l2:
            currentDigit = (sumNode.val + l1.val + l2.val)%10
            nextDigit = (sumNode.val + l1.val + l2.val)//10

            sumNode.val = currentDigit
            if nextDigit>0:
                sumNode.next = ListNode(nextDigit)
            elif l1.next or l2.next:
                sumNode.next = ListNode(0)
            sumNode = sumNode.next
            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            l = l1 if l1 else l2
            while l:
                currentDigit = (sumNode.val + l.val)%10
                nextDigit = (sumNode.val + l.val)//10
                sumNode.val = currentDigit
                if l.next or nextDigit>0:
                    sumNode.next = ListNode(nextDigit)
                l = l.next
                sumNode = sumNode.next
        
        return sumNodeHead
        
        
        
        