# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         '''
#         greedy
#         '''
#         n = len(nums)
#         if n <= 1:
#             return n

#         len_max = 1
#         up = None
#         for i in range(1,n):
#             if nums[i] > nums[i-1] and up != True:
#                 len_max += 1
#                 up = True
#             if nums[i] < nums[i-1] and up != False:
#                 len_max += 1
#                 up = False
#         return len_max


# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         '''
#         dp
#         1. record the longest wiggle sequence ends at i with last step up
#         2. record the longest wiggle sequence ends at i with last step down
#         '''
#         n = len(nums)
#         # exceptions
#         if n <= 1:
#             return 1

#         # dp traversal
#         up = [1 for i in range(n)]
#         down = [1 for i in range(n)]

#         for i in range(1, n):
#             for j in range(i):
#                 if nums[j] > nums[i]:
#                     up[i] = max(up[i], down[j] + 1)
#                 elif nums[j] < nums[i]:
#                     down[i] = max(down[i], up[j] + 1)
#         return max(up[n - 1], down[n - 1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        dp, O(n)
        """
        n = len(nums)
        # exceptions
        if n <= 1:
            return 1

        # dp traversal
        up = [1 for i in range(n)]
        down = [1 for i in range(n)]

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i - 1] > nums[i]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
            # print(up, down)
        return max(up[n - 1], down[n - 1])
