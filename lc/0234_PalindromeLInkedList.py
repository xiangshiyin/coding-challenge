# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         curr = head
#         cache = []
#         while curr:
#             cache.append(curr.val)
#             curr = curr.next
#         # print(cache)
        
#         # check if it is palindrome
#         return cache == cache[::-1]

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        cache = []
        while curr:
            cache.append(curr.val)
            curr = curr.next
        # print(cache)
        
        # check if it is palindrome
        l = 0
        r = len(cache) - 1
        while l < r and cache[l]==cache[r]:
            l += 1
            r -= 1
        if l>r or l==r:
            return True
        else:
            return False
        
            
        
    