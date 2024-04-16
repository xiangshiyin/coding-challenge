# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        ## bfs traversal
        ans = []
        q = deque()
        if not root:
            ans.append('null')
        else:
            q.append(root)
            while q:
                node = q.popleft()
                if not node:
                    ans.append('null')
                else:
                    ans.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
        return ','.join(ans)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = deque([int(val) if val != 'null' else None for val in data.split(',')])
        # print(vals)
        
        val_root = vals.popleft()
        root = TreeNode(val_root) if val_root != None else None
        if root:
            q = deque([root])
            while q:
                node = q.popleft()
                if node:
                    lv, rv = vals.popleft(), vals.popleft()
                    node.left = TreeNode(lv) if lv != None else None
                    node.right = TreeNode(rv) if rv != None else None
                    q.append(node.left)
                    q.append(node.right)
                    
        return root
    
    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
