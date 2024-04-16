#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s2 = s.split()
        if len(s2) != len(pattern):
            return False
        pairs = {}
        seen = set()
        for i in range(len(pattern)):
            if s2[i] not in seen and pattern[i] not in pairs:
                pairs[pattern[i]] = s2[i]
                seen.add(s2[i])
            elif not (
                s2[i] in seen and pattern[i] in pairs and pairs[pattern[i]] == s2[i]
            ):
                return False
        return True


# @lc code=end
