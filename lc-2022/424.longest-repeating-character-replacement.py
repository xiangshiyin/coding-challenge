#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        n = len(s)
        l = 0
        r = 0
        max_L = 0
        seen = defaultdict(int)
        maxCount = 0
        while l <= r and r < n:
            seen[s[r]] += 1
            maxCount = max(maxCount, seen[s[r]])
            while r - l + 1 - maxCount > k:
                seen[s[l]] -= 1
                l += 1
            max_L = max(max_L, r - l + 1)
            r += 1

        return max_L


# @lc code=end

