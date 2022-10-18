#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        ans = strs[0]
        for i in range(1, n):
            j = 0
            for ch in strs[i]:
                if j == len(ans) or ch != ans[j]:
                    break
                j += 1
            if j < len(ans):
                ans = ans[:j]

        return ans


# @lc code=end
