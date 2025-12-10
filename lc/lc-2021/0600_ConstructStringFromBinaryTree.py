# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def tree2str(self, t: TreeNode) -> str:
#         def buildTree(node):
#             ans = ''
#             if node:
#                 if not node.left and not node.right:
#                     ans = f'{node.val}'
#                 elif node.left and node.right:
#                     ans = f'{node.val}({buildTree(node.left)})({buildTree(node.right)})'
#                 elif not node.left:
#                     ans = f'{node.val}()({buildTree(node.right)})'
#                 else:
#                     ans = f'{node.val}({buildTree(node.left)})'
#             return ans

#         return buildTree(t)


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        """
        use stack, inorder traversal
        """
        stack = [t]
        visited = set()
        ans = ""

        if not t:
            return ""

        while stack:
            top = stack[-1]
            if top in visited:
                stack.pop()
                ans += ")"
            else:
                visited.add(top)
                ans += f"({top.val}"
                if not top.left and top.right:
                    ans += "()"
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
        return ans[1:-1]
