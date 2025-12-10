# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         '''
#         dp solution, O(n2) space
#         '''
#         N = len(s)
#         answer = [[0]*N for i in range(N)]

#         for l in range(1, N + 1):
#             for i in range(N - l + 1):
#                 j = i + l -1
#                 if i == j:
#                     answer[i][j] = 1
#                 else:
#                     if s[i] == s[j] and j > i + 1:
#                         answer[i][j] = answer[i + 1][j - 1] + 2
#                     elif s[i] == s[j] and j == i + 1:
#                         answer[i][j] = 2
#                     elif s[i] != s[j] and j > i + 1:
#                         answer[i][j] = max(answer[i + 1][j], answer[i][j - 1])
#                     else:
#                         answer[i][j] = 1
#         return answer[0][N-1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        dp solution, O(n2) space
        """
        N = len(s)
        answer = [[0] * N for i in range(N)]

        dp0 = [0] * N
        dp1 = [0] * N
        dp2 = [0] * N

        for l in range(1, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                if i == j:
                    dp0[i] = 1
                else:
                    if s[i] == s[j] and j > i + 1:
                        dp0[i] = dp2[i + 1] + 2
                    elif s[i] == s[j] and j == i + 1:
                        dp0[i] = 2
                    elif s[i] != s[j] and j > i + 1:
                        dp0[i] = max(dp1[i + 1], dp1[i])
                    else:
                        dp0[i] = 1

            tmp = dp2
            dp2 = dp1
            dp1 = dp0
            dp0 = tmp

        return dp1[0]
