"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # handle the exceptions
        if arr == None or arr == []:
            return None

        # traverse the list
        maxValue = 0
        for idx in range(len(arr) - 1, -1, -1):
            if idx == len(arr) - 1:  # 1st iteration
                maxValue = arr[idx]
                arr[idx] = -1
            else:
                tmp = arr[idx]
                arr[idx] = maxValue  # update element value
                if tmp > maxValue:  # update the max value
                    maxValue = tmp
        return arr
