class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        dfs, bottom up, record the shortest sum at each level
        """
        n = len(triangle)
        # special case
        if n == 1:
            return triangle[0][0]

        from collections import defaultdict

        visited = {}

        def dfs(level, idx):
            res = triangle[level][idx]
            if level == n - 1:
                visited[(level, idx)] = res
                return res

            lres = (
                dfs(level + 1, idx)
                if (level + 1, idx) not in visited
                else visited[(level + 1, idx)]
            )
            rres = (
                -1e5
                if idx + 1 == len(triangle[level + 1])
                else dfs(level + 1, idx + 1)
                if (level + 1, idx + 1) not in visited
                else visited[(level + 1, idx + 1)]
            )

            res += min(lres, rres)
            visited[(level, idx)] = res
            return res

        return dfs(0, 0)
