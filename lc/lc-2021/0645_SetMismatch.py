# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         n = len(nums)
        
#         from collections import Counter
#         freq = Counter(nums)
        
#         presents = set()
#         res = []
#         for num in freq.keys():
#             presents.add(num)
#             if freq[num] > 1:
#                 res.append(num)
#         res.extend(set(range(1,n+1)) - presents)
        
#         return res

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]
