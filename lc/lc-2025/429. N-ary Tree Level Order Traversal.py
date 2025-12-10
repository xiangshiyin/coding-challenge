from collections import deque


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        output = []
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            tmp = []
            for i in range(l):
                curr = q.popleft()
                tmp.append(curr.val)
                if curr.children:
                    for c in curr.children:
                        q.append(c)
            output.append(tmp)
        return output
