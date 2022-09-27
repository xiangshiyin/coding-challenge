#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        saw = defaultdict(list)
        for s in strs:
            encode = self.encode(s)
            saw[encode].append(s)
        return list(saw.values())

    def encode(self, s):
        pattern = [0] * 26
        for ch in s:
            pattern[ord(ch) - ord("a")] += 1
        return str(pattern)


# @lc code=end
