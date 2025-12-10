"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:
    """
    only beats 5%
    """

    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []
        from collections import deque

        ## can we first figure out the N value?
        self.N = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                self.N = max(self.N, len(node.children))
                if len(node.children) > 0:
                    for c in node.children:
                        q.append(c)

        # serialize the tree
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append("null")
            else:
                res.append(str(node.val))
                for c in node.children:
                    q.append(c)
                nc = len(node.children)  # num of children
                while nc < self.N:
                    q.append(None)
                    nc += 1

        return ",".join(res)

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        from collections import deque

        vals = deque([eval(v) if v != "null" else None for v in data.split(",")])
        # print(vals)
        val_root = vals.popleft()
        if val_root == None:
            return None

        # print(self.N)
        root = Node(val_root, [])
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                if self.N > 0:
                    children = [vals.popleft() for i in range(self.N)]
                    if children[0] != None:  # have children
                        for c in children:
                            if c != None:
                                child = Node(c, [])
                                node.children.append(child)
                                q.append(child)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
