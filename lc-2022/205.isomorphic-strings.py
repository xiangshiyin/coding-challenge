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
        map = {}
        for i in range(n):
            if s[i] not in map and t[i] not in saw:
                map[s[i]] = t[i]
            elif s[i] in map and map[s[i]] != t[i]:
                return False
            elif s[i] not in map and t[i] in saw:
                return False
            saw.add(t[i])
        return True

        
# @lc code=end

