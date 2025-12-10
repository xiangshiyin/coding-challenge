# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         '''
#         Time limit exceeded
#         '''
#         n = len(nums)
#         counter = 0
#         q = [(0,S)]

#         while q:
#             # pop
#             idx, target = q.pop()

#             # evaluate
#             if idx == n - 1:
#                 if nums[idx] == target or -1 * nums[idx] == target:
#                     counter += 1
#                     if target == 0:
#                         counter += 1

#             # add children
#             if idx + 1 < n:
#                 q.append((idx + 1, target + nums[idx]))
#                 q.append((idx + 1, target - nums[idx]))


#         return counter


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        dp
        """
        n = len(nums)
        max_sum = sum(nums)
        print(2 * max_sum + 1)

        if max_sum < S:
            return 0
        grid = [[0] * (2 * max_sum + 1) for i in range(n + 1)]
        grid[0][max_sum] = 1

        for i in range(n):
            for j in range(nums[i], 2 * max_sum + 1 - nums[i]):
                if grid[i][j] > 0:
                    grid[i + 1][j + nums[i]] += grid[i][j]
                    grid[i + 1][j - nums[i]] += grid[i][j]

        return grid[n][S + max_sum]
