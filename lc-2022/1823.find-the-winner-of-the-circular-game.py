#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         from collections import deque

#         q = deque(range(1, n + 1))
#         L = len(q)
#         idx = 1
#         while q and L > 1:
#             v = q.popleft()
#             if idx % k != 0:
#                 q.append(v)
#             else:
#                 L -= 1
#             idx += 1
#         return q[0]


# solution on 2022-10-03
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        vs = list(range(1, n + 1))
        L = n
        while L > 1:
            idx = (k - 1) % L
            vs = vs[idx + 1 :] + vs[:idx]
            L -= 1
        return vs[0]


# @lc code=end
