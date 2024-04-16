# class Solution:
#     ## with division
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         N = len(nums)
        
#         # traverse the list
#         ## 1st pass, get the total product
#         total_prod = 1
#         zero_counter = 0
#         for num in nums:
#             if zero_counter>1:
#                 return [0 for i in range(N)]
#             if num==0:
#                 zero_counter += 1
#             else:
#                 total_prod = total_prod*num
#         ## 2nd pass, generate the output
#         if zero_counter==0:
#             return [total_prod//num for num in nums]
#         elif zero_counter>1:
#             return [0 for i in range(N)]
#         else:
#             return [0 if num!=0 else total_prod for num in nums]
        
class Solution:
    ## without division
    def productExceptSelf(self, nums: List[int]) -> List[int]:   
        N = len(nums)
        # 1st pass get the left side prod
        output = []
        zero_counter = 0
        for idx in range(N):
            if nums[idx]==0:
                zero_counter += 1
            if zero_counter>1:
                return [0 for i in range(N)]
            if idx==0:
                output.append(1)
            else:
                output.append(nums[idx-1]*output[-1])
        # 2nd pass get the right side prod
        rprod = 1
        for idx in range(N-1,-1,-1):
            if idx<N-1:
                rprod = rprod*nums[idx+1]
                output[idx] = output[idx]*rprod
        return output
            
        