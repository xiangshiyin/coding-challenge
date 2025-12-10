# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         # exceptions
#         if nums==None:
#             return None
#         n = len(nums)
#         if n==0:
#             return None

#         # find the solution
#         return list(set(range(1,n+1))-set(nums))


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # exceptions
        if nums == None:
            return None
        n = len(nums)
        if n == 0:
            return None

        # find the solution
        tb = {num: 1 for num in nums}
        output = [v for v in range(1, n + 1) if v not in tb]
        return output
