class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # special cases
        if m == 1:
            return matrix[0]
        if n == 1:
            return [matrix[i][0] for i in range(m)]

        dnext = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}

        visited = set()
        p = (0, 0)
        ans = []
        d = (0, 1)

        while len(visited) < m * n:
            # record the grid
            visited.add((p[0], p[1]))
            ans.append(matrix[p[0]][p[1]])
            # check if it should be terminated
            if len(visited) == m * n:
                break

            # find the next step
            while (
                p[0] + d[0] >= m
                or p[0] + d[0] < 0
                or p[1] + d[1] >= n
                or p[1] + d[1] < 0
                or (p[0] + d[0], p[1] + d[1]) in visited
            ):
                d = dnext[d]
            # print(ans, d)

            p = (p[0] + d[0], p[1] + d[1])

        return ans
