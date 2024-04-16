# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         idx = 0
#         len_init = len(arr)
        
#         while idx < len(arr):
#             if arr[idx] != 0:
#                 idx += 1
#             else:
#                 arr.insert(idx+1,0)
#                 idx += 2
#         while len(arr) > len_init:
#             arr.pop()

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # step 1: find out the number of zeros
        zero_counter = 0
        for num in arr:
            if num==0:
                zero_counter += 1
        
        # step 2: move the elements to the right place
        for i in range(len(arr)-1, -1, -1):
            if arr[i]==0:
                zero_counter -= 1
            else:
                tmp = arr[i]
                arr[i] = 0
                if i + zero_counter < len(arr):
                    arr[i + zero_counter] = tmp
            
                
        
            
