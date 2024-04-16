#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heap = []
        L = 0
        for num in nums:
            if L < k:
                heapq.heappush(heap, num)
                L += 1
            else:
                heapq.heappushpop(heap, num)

        return heapq.heappop(heap)


# @lc code=end
