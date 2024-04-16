# class Solution:
#     def minimumDeviation(self, nums: List[int]) -> int:
#         from heapq import heappush, heappop
        
#         pq = []
#         for num in nums:
#             if num % 2 == 1:
#                 heappush(pq, -1 * num * 2)
#             else:
#                 heappush(pq, -1 * num)
        
#         minimum = -1 * max(pq)
#         diff = max(nums)
#         while len(pq) == len(nums):
#             maximum = -1 * heappop(pq)
#             diff = min(diff, maximum - minimum)
#             if maximum % 2 == 0:
#                 minimum = min(minimum, maximum // 2)
#                 heappush(pq, -1 * maximum // 2)
                
#         return diff
            
            
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        from heapq import heappop, heappush
        
        hp = []
        
        # pre-doubling
        for num in nums:
            if num % 2 == 1:
                heappush(hp, -1 * num * 2)
            else:
                heappush(hp, -1 * num)
        
        # division on even numbers
        minimum = -1 * max(hp)
        diff = max(nums) - min(nums)
        
        # loop
        while True:
            maximum = -1 * heappop(hp)
            diff = min(maximum - minimum, diff)
            if maximum % 2 == 0:
                heappush(hp, -1 * maximum // 2)
                minimum = min(minimum, maximum // 2)
            else:
                break
        return diff
            
            
                