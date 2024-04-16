#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        saw = set()
        lookup = {}
        for i in range(n):
            if s[i] not in lookup and t[i] not in saw:
                saw.add(t[i])
                lookup[s[i]] = t[i]
            elif not (s[i] in lookup and t[i] in saw and lookup[s[i]] == t[i]):
                return False

        return True


# @lc code=end

