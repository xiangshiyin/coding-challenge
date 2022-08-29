#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos = -1
        from collections import Counter
        freqs = Counter(s)
        for idx,l in enumerate(s):
            if freqs[l] == 1:
                return idx
        return pos

        
# @lc code=end

