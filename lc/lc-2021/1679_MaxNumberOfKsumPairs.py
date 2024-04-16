# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         # create a look up table
#         helper = {}
#         for num in nums:
#             if num not in helper:
#                 helper[num] = 1
#             else:
#                 helper[num] += 1
        
#         counter = 0
#         # traverse the dictionary
#         for num in helper:
#             if k - num in helper:
#                 if k - num != num:
#                     delta = min(helper[num], helper[k - num])
#                 else:
#                     delta = helper[num]//2
#                 counter += delta
#                 helper[num] -= delta
#                 helper[k - num] -= delta
                        
#         return counter

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         # create a look up table
#         helper = {}
#         for num in nums:
#             if num not in helper:
#                 helper[num] = 1
#             else:
#                 helper[num] += 1
#         # traverse the dictionary
#         counter = 0
#         for num in helper:
#             if k - num in helper:
#                 counter += min(helper[num], helper[k - num])
#         return counter // 2

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        helper = {}
        for num in nums:
            if k - num in helper and helper[k - num] > 0:
                helper[k - num] -= 1
                counter += 1
            else:
                if num not in helper:
                    helper[num] = 1
                else:
                    helper[num] += 1
                    
        return counter
    