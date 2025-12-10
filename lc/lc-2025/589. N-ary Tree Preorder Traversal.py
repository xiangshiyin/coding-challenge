class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        output = [root.val]
        for c in root.children:
            output += self.preorder(c)
        return output
