# class Solution:
#     def createSortedArray(self, instructions: List[int]) -> int:
#         '''
#         The brutal force solution
#         '''
#         # exceptions
#         N = len(instructions)
#         if N<=1:
#             return 0
#         # print(N)
#         # traverse the list
#         cost = 0
#         nums = [-1 for i in range(N)]
#         for i,num in enumerate(instructions):
#             # insert num into nums
#             larger = 0
#             j = N-1
#             if i==0:
#                 nums[i] = num
#             else:
#                 larger = 0
#                 j = i-1
#                 while j>=0:
#                     if nums[j]>num:
#                         nums[j+1] = nums[j]
#                         larger += 1
#                     if nums[j]<num:
#                         break
#                     j -= 1
#                 nums[i-larger] = num

#             # calculate the cost
#             cost +=  min(larger, j+1)
#             # print(num, cost, nums, j+1, i-larger)

#         return cost


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        The python sorted list solution
        """
        from sortedcontainers import SortedList

        sl = SortedList()
        cost = 0

        for num in instructions:
            cost += min(sl.bisect_left(num), len(sl) - sl.bisect_right(num))
            cost = int(cost % (1e9 + 7))
            sl.add(num)
        return cost
