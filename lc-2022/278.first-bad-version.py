#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         l = 1
#         r = n
#         first = n
#         while l <= r:
#             mid = (l + r) // 2
#             if isBadVersion(mid):
#                 first = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return first

# solution on 2022-09-15
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        firstBad = n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                firstBad = min(firstBad, mid)
                r = mid - 1
            else:
                l = mid + 1
        return firstBad


# @lc code=end

