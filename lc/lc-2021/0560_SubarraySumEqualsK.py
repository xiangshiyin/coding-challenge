# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ## brute force method 1: time limit exceeded
#         N = len(nums)
#         count = 0
#         cumsum = []    
#         for i in range(N):
#             if i>0:
#                 for j in range(i):
#                     cumsum[j] += nums[i]
#                     if cumsum[j]==k:
#                         count += 1
#             cumsum.append(nums[i])
#             if cumsum[-1]==k:
#                 count += 1
#             # print(count, cumsum)
#         return count

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ## brute force method 2: time limit exceeded
#         N = len(nums)
#         count = 0
#         cumsum = [0] # length N+1
#         # compute the cumsum at each index
#         for idx in range(N):
#             cumsum.append(cumsum[-1]+nums[idx])
#         # loop through the list, find all the subarray total
#         for i in range(N):
#             for j in range(i+1,N+1):
#                 if cumsum[j]-cumsum[i]==k:
#                     count += 1
#         return count
            
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ## brute force method 3: time limit exceeded
#         N = len(nums)
#         count = 0  
#         for i in range(N):
#             cumsum = 0
#             for j in range(i,N):
#                 cumsum += nums[j]
#                 if cumsum==k:
#                     count += 1
#         return count
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## hash table
        N = len(nums)
        count = 0
        cumsum = 0
        tb = {0:1}
        # build the lookup table on the go
        for num in nums:
            cumsum += num
            if cumsum-k in tb:
                count += tb[cumsum-k]
            # update the lookup table
            if cumsum not in tb:
                tb[cumsum] = 1
            else:
                tb[cumsum] += 1
        return count
    
