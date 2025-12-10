# class Solution:
#     def minOperations(self, n: int) -> int:
#         mean = n
#         ans = 0
#         for i in range(n):
#             if 2 * i + 1 > mean:
#                 ans += 2 * i + 1 - mean
#         return ans


class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            ans = (n + 1 + 2 * n - 1 - 2 * n) * (n // 2) // 2
        else:
            ans = (n + 2 + 2 * n - 1 - 2 * n) * ((n - 1) // 2) // 2

        return ans
