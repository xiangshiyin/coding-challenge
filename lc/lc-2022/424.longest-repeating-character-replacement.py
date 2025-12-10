#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         from collections import defaultdict

#         n = len(s)
#         l = 0
#         r = 0
#         max_L = 0
#         seen = defaultdict(int)
#         maxCount = 0
#         while l <= r and r < n:
#             seen[s[r]] += 1
#             maxCount = max(maxCount, seen[s[r]])
#             while r - l + 1 - maxCount > k:
#                 seen[s[l]] -= 1
#                 l += 1
#             max_L = max(max_L, r - l + 1)
#             r += 1

#         return max_L


# solution on 2022-09-19
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        two pointer, moving window
        """
        n = len(s)
        l = 0
        r = 0
        maxCount = 0
        maxL = 0
        from collections import defaultdict

        freq = defaultdict(int)
        while l <= r and r < n:
            freq[s[r]] += 1
            maxCount = max(maxCount, freq[s[r]])
            while r - l + 1 - maxCount > k:
                freq[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
            r += 1
        return maxL


# @lc code=end
