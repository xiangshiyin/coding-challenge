#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque

        q = deque([(root, 0)])
        ans = []
        L = -1
        while q:
            node, level = q.popleft()
            if not ans or level > L:
                ans.append([node.val])
                L += 1
            else:
                if level % 2 == 0:
                    ans[-1].append(node.val)
                else:
                    ans[-1] = [node.val] + ans[-1]
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return ans


# @lc code=end
