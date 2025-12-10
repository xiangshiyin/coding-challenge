# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         '''
#         O(n2) solution accepted
#         '''
#         N = len(nums)
#         if N<=1:
#             return False
#         else:
#             counter = 0
#             for i in range(N-1):
#                 cumsum = nums[i]
#                 for j in range(i+1,N):
#                     cumsum += nums[j]
#                     if k==0:
#                         if cumsum==0:
#                             counter += 1
#                     elif cumsum%k==0:
#                         counter += 1
#                     if counter>0:
#                         return True
#             return False

# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         '''
#         hash table solution
#         '''
#         N = len(nums)
#         if N<=1:
#             return False
#         else:
#             cumsum = 0
#             if k!=0:
#                 # traverse the list
#                 tb = {}
#                 for idx in range(N):
#                     cumsum += nums[idx]
#                     if cumsum%k==0 and idx>=1: # edge case, be careful
#                         return True
#                     if cumsum%k not in tb:
#                         tb[cumsum%k] = idx
#                     else:
#                         if idx-tb[cumsum%k]>1: # at least length 2
#                             return True
#             else:
#                 tb2 = {}
#                 for idx in range(N):
#                     cumsum += nums[idx]
#                     if cumsum==0 and idx>=1: # edge case, be careful
#                         return True
#                     if cumsum not in tb2:
#                         tb2[cumsum] = idx
#                     else:
#                         if idx-tb2[cumsum]>1: # at least length 2
#                             return True
#             return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        hash table solution, rewrote the previous one
        """
        N = len(nums)
        if N <= 1:
            return False
        else:
            cumsum = 0
            # traverse the list
            tb = {}
            for idx in range(N):
                cumsum += nums[idx]
                # set the target of interest
                if k == 0:
                    target = cumsum
                else:
                    target = cumsum % k
                # check the condition
                if target == 0 and idx >= 1:  # edge case, be careful
                    return True
                if target not in tb:
                    tb[target] = idx
                else:
                    if idx - tb[target] > 1:  # at least length 2
                        return True
            return False
