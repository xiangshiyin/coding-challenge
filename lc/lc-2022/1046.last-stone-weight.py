#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [-1 * s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 != s2:
                heapq.heappush(stones, -1 * abs(s1 - s2))
        return -1 * stones[0] if stones else 0


# @lc code=end
