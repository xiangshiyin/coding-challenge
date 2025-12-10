# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
#         '''
#         3 pass traversal, not so fast but use very little memory
#         '''
#         output = []
#         # step 1: get the left boundary
#         if root.left:
#             node = root
#             while node:
#                 output.append(node)
#                 if node.left:
#                     node = node.left
#                 else:
#                     node = node.right
#         else:
#             output.append(root)


#         # step 2: get the bottom boundary
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.left == None and node.right == None and node != output[-1]:
#                 output.append(node)
#             ## add the children
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)

#         # step 3: get the residual right boundary
#         ## accumulate the stack of right children
#         stack = []
#         node = root.right
#         while node:
#             stack.append(node)
#             if node.right:
#                 node = node.right
#             else:
#                 node = node.left
#         ## populate the right boundary
#         while stack:
#             node = stack.pop()
#             if node != output[-1]:
#                 output.append(node)


#         return [n.val for n in output]


# class Solution:
#     def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
#         '''
#         both running time and memory usage are not ideal

#         strategy
#         1. pre-order traversal of the left boundary
#         2. post-order traversal of the bottom boundary
#         3. in-order traversal of the right boundary
#         '''
#         output = [root]

#         # step 1: left boundary
#         node = root.left
#         while node:
#             if node.left != None or node.right != None:
#                 output.append(node)

#             if node.left:
#                 node = node.left
#             else:
#                 node = node.right


#         # step 2: bottom boundary
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.left == None and node.right == None and node != root:
#                 output.append(node)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)

#         # print([n.val for n in output])

#         # step 3: right boundary
#         def getRight(node):
#             res = []
#             if node:
#                 if node.right:
#                     res += getRight(node.right)
#                 else:
#                     res += getRight(node.left)

#                 if (node.left != None or node.right != None) and node != root:
#                     res.append(node)

#             return res

#         output += getRight(root.right)

#         return [node.val for node in output]

# class Solution:
#     def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
#         '''
#         both running time and memory usage are not ideal

#         strategy
#         1. pre-order traversal of the left boundary
#         2. post-order traversal of the bottom boundary
#         3. in-order traversal of the right boundary
#         '''
#         output = [root]

#         # step 1: left boundary
#         def getLeft(node):
#             res = []
#             if node and (node.left != None or node.right != None):
#                 res.append(node)
#                 if node.left:
#                     res += getLeft(node.left)
#                 else:
#                     res += getLeft(node.right)
#             return res

#         output += getLeft(root.left)


#         # step 2: bottom boundary
#         def getBottom(node):
#             res = []
#             if node:
#                 if node.left:
#                     res += getBottom(node.left)
#                 if node.right:
#                     res += getBottom(node.right)
#                 if node.left == None and node.right == None and node != root:
#                     res.append(node)
#             return res

#         output += getBottom(root)


#         # step 3: right boundary
#         def getRight(node):
#             res = []
#             if node:
#                 if node.right:
#                     res += getRight(node.right)
#                 else:
#                     res += getRight(node.left)

#                 if (node.left != None or node.right != None) and node != root:
#                     res.append(node)

#             return res

#         output += getRight(root.right)

#         return [node.val for node in output]


# class Solution:
#     def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
#         '''
#         both running time and memory usage are not ideal

#         strategy
#         1. pre-order traversal of the left boundary
#         2. post-order traversal of the bottom boundary
#         3. in-order traversal of the right boundary
#         '''
#         output = [root]

#         # step 1: left boundary
#         def getLeft(node):
#             if node and (node.left != None or node.right != None):
#                 output.append(node)
#                 if node.left:
#                     getLeft(node.left)
#                 else:
#                     getLeft(node.right)

#         getLeft(root.left)

#         # step 2: bottom boundary
#         def getBottom(node):
#             if node:
#                 if node.left:
#                     getBottom(node.left)
#                 if node.right:
#                     getBottom(node.right)
#                 if node.left == None and node.right == None and node != root:
#                     output.append(node)

#         getBottom(root)


#         # step 3: right boundary
#         def getRight(node):
#             if node:
#                 if node.right:
#                     getRight(node.right)
#                 else:
#                     getRight(node.left)

#                 if (node.left != None or node.right != None) and node != root:
#                     output.append(node)

#         getRight(root.right)

#         return [node.val for node in output]


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        """
        both running time and memory usage are not ideal

        strategy
        1. pre-order traversal of the left boundary
        2. post-order traversal of the bottom boundary
        3. in-order traversal of the right boundary
        """
        output = [root.val]

        # step 1: left boundary
        def getLeft(node):
            if node and (node.left != None or node.right != None):
                output.append(node.val)
                if node.left:
                    getLeft(node.left)
                else:
                    getLeft(node.right)

        getLeft(root.left)

        # step 2: bottom boundary
        def getBottom(node):
            if node:
                if node.left:
                    getBottom(node.left)
                if node.right:
                    getBottom(node.right)
                if node.left == None and node.right == None and node != root:
                    output.append(node.val)

        getBottom(root)

        # step 3: right boundary
        def getRight(node):
            if node:
                if node.right:
                    getRight(node.right)
                else:
                    getRight(node.left)

                if (node.left != None or node.right != None) and node != root:
                    output.append(node.val)

        getRight(root.right)

        return output
