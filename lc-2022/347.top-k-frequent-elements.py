#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        freq = Counter(nums)

        return heapq.nlargest(k, freq.keys(), lambda key: freq[key])


# @lc code=end
