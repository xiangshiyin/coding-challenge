# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        ## bfs
        res = []
        from collections import deque

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                res.append("null")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        # print(','.join(res))
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        ## bfs
        from collections import deque

        vals = deque([eval(v) if v != "null" else None for v in data.split(",")])
        if vals[0] == None:
            return None

        val_root = vals.popleft()
        root = TreeNode(val_root)
        q = deque([root])
        while vals:
            node = q.popleft()
            if node:
                lv, rv = vals.popleft(), vals.popleft()
                l = TreeNode(val=lv) if lv != None else None
                r = TreeNode(val=rv) if rv != None else None
                node.left = l
                node.right = r
                q.append(l)
                q.append(r)

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
