'''
Classic tree traverse exercise!!!
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         '''
#         recursive inorder traverse
#         '''
#         self.output = None
#         def inorder(o: TreeNode, c: TreeNode):
#             if o:
#                 inorder(o.left, c.left)
#                 if o is target:
#                     self.output = c
#                     return
#                 inorder(o.right, c.right)
        
#         # call the function
#         inorder(original, cloned)
#         return self.output

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         '''
#         recursive preorder traverse
#         '''
#         self.output = None
#         def preorder(o: TreeNode, c: TreeNode):
#             if o:
#                 if o is target:
#                     self.output = c
#                     return
#                 preorder(o.left, c.left)
#                 preorder(o.right, c.right)
#         # call the function
#         preorder(original, cloned)
#         return self.output


# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         '''
#         iterative inorder traverse
#         '''                
#         stack_o,stack_c = [],[]
#         node_o,node_c = original,cloned
        
#         while stack_o or node_o:
#             # traverse the left branch
#             while node_o:
#                 stack_o.append(node_o)
#                 stack_c.append(node_c)
                
#                 node_o = node_o.left
#                 node_c = node_c.left
#             # pull a node
#             node_o = stack_o.pop()
#             node_c = stack_c.pop()
            
#             if node_o == target:
#                 return node_c
            
#             # traverse the right branch
#             node_o = node_o.right
#             node_c = node_c.right
        
# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         '''
#         iterative inorder bfs traverse
#         '''         
#         from collections import deque
#         queue_o,queue_c = deque([original]),deque([cloned])
        
#         while queue_o:
#             node_o = queue_o.popleft()
#             node_c = queue_c.popleft()
            
#             if node_o is target:
#                 return node_c
            
#             if node_o:
#                 queue_o.append(node_o.left)
#                 queue_o.append(node_o.right)
            
#                 queue_c.append(node_c.left)
#                 queue_c.append(node_c.right)
                

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        '''
        recursive traverse rewrite
        '''       
        if not original:
            return None
        if original is target:
            return cloned
        
        # the left child
        output = self.getTargetCopy(original.left, cloned.left, target)
        if output:
            return output
        else:
            return self.getTargetCopy(original.right, cloned.right, target)
