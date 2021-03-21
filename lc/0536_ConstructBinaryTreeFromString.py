# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        
        def buildTree(s):
            # find the first left bracket
            ix = s.find('(')
            if ix < 0:
                return TreeNode(int(s)) if s else None
            
            lcounter = 1
            rcounter = 0
            jx = ix + 1 
            while jx < len(s) and lcounter >= rcounter:
                if s[jx] == '(':
                    lcounter += 1
                elif s[jx] == ')':
                    rcounter += 1
                
                if rcounter == lcounter:
                    break
                jx += 1
            
            if s[:ix] != '':
                root = TreeNode(s[:ix])
                root.left = buildTree(s[ix+1:jx])
                root.right = buildTree(s[jx+1:-1])
            else:
                root = buildTree(s[ix+1:jx])
            
            return root
        
        return buildTree(s)

# class Solution:
#     '''
#     Modified version
#     '''
#     def str2tree(self, s: str) -> TreeNode:
        
#         def buildTree(s):
#             # find the first left bracket
#             ix = s.find('(')
#             if ix < 0:
#                 return TreeNode(int(s)) if s else None
            
#             unmatched = 1
#             jx = ix + 1 
#             while jx < len(s):
#                 if s[jx] == '(':
#                     unmatched += 1
#                 elif s[jx] == ')':
#                     unmatched -= 1
                
#                 if unmatched == 0:
#                     break
#                 jx += 1
                
#             root = TreeNode(s[:ix])
#             root.left = buildTree(s[ix+1:jx])
#             root.right = buildTree(s[jx+2:-1])
            
#             return root
        
#         node = buildTree(s)
        
#         return node

                
# class Solution:
#     '''
#     solution from others
#     '''
#     def str2tree(self, S):
#         ix = S.find('(')
#         if ix < 0:
#             return TreeNode(int(S)) if S else None

#         bal = 0
#         for jx, u in enumerate(S):
#             if u == '(': bal += 1
#             if u == ')': bal -= 1
#             if jx > ix and bal == 0:
#                 break

#         root = TreeNode(int(S[:ix]))
#         root.left = self.str2tree(S[ix+1:jx])
#         root.right = self.str2tree(S[jx+2:-1])
#         return root    
        
        
        