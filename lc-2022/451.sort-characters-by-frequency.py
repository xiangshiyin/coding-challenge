#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        bucket sort
        """
        from collections import Counter, defaultdict

        freq = Counter(s)
        buckets = defaultdict(list)
        for ch, f in freq.items():
            buckets[f].append(ch)

        ans = ""
        l = len(s)
        while l > 0:
            while not buckets[l]:
                l -= 1

            if l == 0:
                break
            for ch in buckets[l]:
                ans += ch * l
            if len(ans) == len(s):
                break
            l -= 1

        return ans


# @lc code=end
