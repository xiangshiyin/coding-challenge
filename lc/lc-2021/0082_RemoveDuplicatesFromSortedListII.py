# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # handle exceptions
        if head==None or head.next==None:
            return head
        
        prehead = ListNode(val=-1000, next=head)
        pre = prehead
        curr = head
        post = head.next
        counter = 1
        
        while post:
            # traverse continuous duplicates
            while post.val==curr.val:
                post = post.next
                counter += 1
                if post==None:
                    break
                
            if post:
                if counter==1: # if no continuous duplicates exist
                    pre = curr
                    curr = post
                else:
                    curr = post # if continuous duplicates exist
                    pre.next = curr
                    counter = 1
                post = post.next
            else:
                if counter==1:
                    curr.next = None
                else:
                    pre.next = None
                break
        
        return prehead.next
            
        
        
                
                
            
        
        
            
            
            
        
        
            
        
        
                
        
        