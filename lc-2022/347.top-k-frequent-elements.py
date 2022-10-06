#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         import heapq
#         from collections import Counter

#         freq = Counter(nums)

#         return heapq.nlargest(k, freq.keys(), lambda key: freq[key])


# solution on 2022-10-05
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter, defaultdict

        freq = Counter(nums)
        buckets = defaultdict(list)
        for v, f in freq.items():
            buckets[f].append(v)

        n = len(nums)
        bucketIndex = n
        ans = []
        while k > 0:
            while not buckets[bucketIndex]:
                bucketIndex -= 1
            for num in buckets[bucketIndex]:
                if k == 0:
                    break
                ans.append(num)
                k -= 1
            bucketIndex -= 1
        return ans


# @lc code=end
