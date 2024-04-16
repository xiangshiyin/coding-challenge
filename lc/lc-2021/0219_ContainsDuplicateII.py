# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         # create hash table on index
#         tb = {}
#         pairExists = 0
#         for i,num in enumerate(nums):
#             if num not in tb:
#                 tb[num] = [i]
#             else:
#                 tb[num].append(i)
#                 if tb[num][-1] - tb[num][-2] <= k:
#                     return True
                    
#         return False


# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         '''
#         Much less memory, but still not ideal on speed
#         '''
#         # create hash table on index
#         tb = {}
#         pairExists = 0
#         for i,num in enumerate(nums):
#             if num not in tb:
#                 tb[num] = i
#             else:
#                 if i - tb[num] <= k:
#                     return True
#                 tb[num] = i
                    
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Much less memory, beats 97% in speed
        '''
        # create hash table on index
        tb = {}
        pairExists = 0
        for i,num in enumerate(nums):
            if num in tb and i - tb[num] <= k:
                    return True
            tb[num] = i
                    
        return False
    
    
    