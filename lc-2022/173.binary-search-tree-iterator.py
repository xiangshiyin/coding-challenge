#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class BSTIterator:
#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = []
#         self.pushLeftBranch(root)

#     def pushLeftBranch(self, root: Optional[TreeNode]):
#         while root:
#             self.stack.append(root)
#             root = root.left

#     def next(self) -> int:
#         node = self.stack.pop()
#         self.pushLeftBranch(node.right)
#         return node.val

#     def hasNext(self) -> bool:
#         return len(self.stack) > 0


# solution on 2022-10-25
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeftBranch(root)

    def pushLeftBranch(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if len(self.stack) > 0:
            node = self.stack.pop()
            self.pushLeftBranch(node.right)
            return node.val
        else:
            return

    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
