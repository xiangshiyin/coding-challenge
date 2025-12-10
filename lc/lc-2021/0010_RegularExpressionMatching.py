class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        dp
        """
        s = " " + s
        p = " " + p
        dp = [[0] * len(p) for i in range(len(s))]
        dp[0][0] = 1

        # initialize the 1st row
        for i in range(1, len(p)):
            if p[i] == "*":
                dp[0][i] = dp[0][i - 2]

        # traverse the grids
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if s[i] == p[j - 1] or p[j - 1] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        # print(dp)
        return dp[-1][-1]
