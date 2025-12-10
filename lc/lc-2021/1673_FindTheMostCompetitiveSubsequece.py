# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         '''
#         brutal force, time limit exceeded
#         '''
#         N = len(nums)

#         start = 0
#         output = []
#         while k > 0:
#             for i in range(start, N - k + 1):
#                 if i == start:
#                     pick = i
#                 else:
#                     if nums[i] < nums[pick]:
#                         pick = i
#             output.append(nums[pick])
#             start = pick + 1
#             k -= 1
#         return output


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        stack solution
        """
        N = len(nums)

        # traverse the list
        stack = []
        skipped = 0
        for i, num in enumerate(nums):
            while stack and num < stack[-1] and skipped < N - k:
                pop = stack.pop()
                skipped += 1
            stack.append(num)

        return stack[:k]
