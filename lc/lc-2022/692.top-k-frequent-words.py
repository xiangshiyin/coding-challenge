#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        freq = Counter(words)

        import heapq

        ans_raw = heapq.nsmallest(k, freq, key=lambda w: (-1 * freq[w], w))
        return ans_raw


# @lc code=end

