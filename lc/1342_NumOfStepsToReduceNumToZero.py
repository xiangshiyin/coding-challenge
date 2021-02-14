# class Solution:
#     def numberOfSteps (self, num: int) -> int:
#         '''
#         General Math
#         '''
#         if num == 0:
#             return 0
        
#         step = 0
#         while num > 0:
#             if num % 2 == 0:
#                 num = num //2
#             else:
#                 num = num - 1 
#             step += 1
#         # print(step)
        
#         return step
    
class Solution:
    def numberOfSteps (self, num: int) -> int:
        '''
        Bitwise operation
        '''
        step = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num = (num >> 1)
            step += 1
        return step
    