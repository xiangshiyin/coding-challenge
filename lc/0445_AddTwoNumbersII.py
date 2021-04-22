# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        stack
        '''
        
        # build the stacks
        h1 = l1
        s1 = []
        n1 = 0
        while h1:
            s1.append(h1)
            h1 = h1.next
            n1 += 1
            
        h2 = l2
        s2 = []
        n2 = 0
        while h2:
            s2.append(h2)
            h2 = h2.next
            n2 += 1
        
        # calculate the summation
        ls = s1 if n1 >= n2 else s2 # left stack, the longer one
        rs = s2 if n1 >= n2 else s1 # right stack
        delta = 0
        
        while ls and rs:
            l = ls.pop()
            r = rs.pop()
            tmp = l.val + r.val + delta
            l.val = tmp % 10
            delta = tmp // 10
        
        if not ls and delta:
            h = ListNode(val=delta, next=l)
        else:
            while ls:
                l = ls.pop()
                tmp = l.val + delta
                l.val = tmp % 10
                delta = tmp // 10
            if not delta:
                h = l
            else:
                h = ListNode(val=delta, next=l)
        return h
    
            
            
        
        
        
        