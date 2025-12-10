# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # bad solution with time limit exceeded
#         N = len(nums)
#         if N>1 and k>0:
#             while k>0:
#                 target = nums[N-1]
#                 for idx in range(N-1,0,-1):
#                     nums[idx] = nums[idx-1]
#                 nums[0] = target
#                 k -= 1


# # solution 1: 12/28/2020
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         N = len(nums)
#         k2 = k%N # the actual number of steps to move

#         if N>1 and k2>0:
#             start = 0
#             idx_source = 0
#             source = nums[idx_source]
#             counter = 0

#             while counter<N:
#                 # compute the target slot
#                 idx_target = (idx_source+k2)%N
#                 # print(idx_source, idx_target, counter)
#                 # cache the target slot value
#                 tmp = nums[idx_target]
#                 # change the target slot value
#                 nums[idx_target] = source
#                 # update the source values
#                 if idx_target==start:
#                     start += 1 # reset the iteration
#                     idx_source = start
#                     source = nums[idx_source]
#                 else:
#                     idx_source = idx_target
#                     source = tmp

#                 # update the counter
#                 counter += 1


# solution 2: 12/28/2020
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k2 = k % N  # the actual number of steps to move

        if N > 1 and k2 > 0:
            self.reverse(nums, 0, N - 1)
            self.reverse(nums, 0, k2 - 1)
            self.reverse(nums, k2, N - 1)


# solution as of 11/12/2021
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # get effective k
        k = k % n

        # exceptions
        if n == 1:
            return nums

        # we can do 3 flips to achieve the rotation
        ## define the flip function
        def flip(vs, l, r):
            while l < r:
                vs[l], vs[r] = vs[r], vs[l]
                l += 1
                r -= 1

        # step 1: full flip
        flip(nums, 0, n - 1)
        # step 2: flip the head
        flip(nums, 0, k - 1)
        # step 3: flip the tail
        flip(nums, k, n - 1)

        return nums
