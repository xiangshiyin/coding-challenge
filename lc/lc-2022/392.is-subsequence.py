#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        pt = 0
        while ps < len(s) and pt < len(t):
            while pt < len(t) and t[pt] != s[ps]:
                pt += 1
            if pt < len(t):
                ps += 1
                pt += 1
            else:
                return False

        if ps == len(s):
            return True
        else:
            return False


# @lc code=end

