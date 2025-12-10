"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # deal with exceptions
        if arr == None:
            return False
        if len(arr) < 3:
            return False
        # traverse the list
        flg_desc = 0

        for idx in range(1, len(arr)):
            if arr[idx] == arr[idx - 1]:
                return False
            if flg_desc == 0:
                if (idx == 1) & (arr[idx] < arr[idx - 1]):
                    return False
                if (idx > 1) & (arr[idx] < arr[idx - 1]):
                    flg_desc = 1
            else:
                if arr[idx] > arr[idx - 1]:
                    return False
            # print(idx, flg_desc, flg_plateau)
        if flg_desc == 0:
            return False
        return True


# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         # deal with exceptions
#         if arr==None:
#             return False
#         if len(arr)<3:
#             return False
#         # traverse the list upward
#         idx = 0
#         while idx<len(arr)-1 and arr[idx]<arr[idx+1]:
#             idx += 1
#             print(idx)

#         # check
#         if idx==0 or idx==len(arr)-1:
#             return False

#         # traverse the list downward:
#         while idx<len(arr)-1 and arr[idx]>arr[idx+1]:
#             idx += 1

#         # check
#         if idx < len(arr)-1:
#             return False

#         return True
