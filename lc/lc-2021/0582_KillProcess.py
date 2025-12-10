class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        post-order traversal
        """
        # create hash table to find all children of a given process
        p2c = {}
        for i in range(len(ppid)):
            if ppid[i] not in p2c:
                p2c[ppid[i]] = [pid[i]]
            else:
                p2c[ppid[i]].append(pid[i])

        # print(p2c)

        def postorder(node):
            res = []
            if node in p2c:
                for child in p2c[node]:
                    res += postorder(child)
            res.append(node)

            return res

        return postorder(kill)
