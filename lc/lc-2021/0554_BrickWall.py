class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # traverse the wall row by row, accumulate the frequency of right boundary frequency
        from collections import defaultdict

        tb = defaultdict(int)

        m = len(wall)
        n = len(wall[0])
        for i in range(m):
            presum = 0
            j = 0
            while j < len(wall[i]) - 1:
                presum += wall[i][j]
                # print(i, presum)
                tb[presum] += 1
                j += 1
        # print(tb)

        # find the col index where most of boundaries are located
        col = 0
        nocross = 0
        for k, v in tb.items():
            if v >= nocross:
                nocross = v
                col = k
        # print(col, nocross)
        return m - nocross
