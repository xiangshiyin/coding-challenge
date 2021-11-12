# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         N = len(numbers)
#         low = 0
#         high = N-1
#         while low<high:
#             if numbers[low]+numbers[high]<target:
#                 low += 1
#             elif numbers[low]+numbers[high]==target:
#                 return[low+1,high+1]
#             else:
#                 high -= 1
#         return [-1,-1]

# solution as of 11/12/2021
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        2 pointer, no extra memory consumption
        '''
        n = len(numbers)
        l = 0
        r = n - 1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

                
                
