# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        """
        BFS plus hash table
        """

        from collections import deque, defaultdict

        tb = defaultdict(list)
        queue = deque()
        queue.append([0, root])

        while queue:
            q_tmp = []
            tb_tmp = defaultdict(list)

            while queue:
                # populate tmp queue
                x, node = queue.popleft()

                # update tmp hash table
                tb_tmp[x].append(node.val)

                # add childrens to tmp queue
                if node.left:
                    q_tmp.append([x - 1, node.left])

                if node.right:
                    q_tmp.append([x + 1, node.right])

            # update queue and tb
            for key in tb_tmp:
                tb[key].extend(sorted(tb_tmp[key]))

            queue.extend(q_tmp)

        # generate return value
        return [tb[key] for key in sorted(tb.keys())]
