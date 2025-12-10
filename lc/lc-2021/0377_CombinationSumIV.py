# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         '''
#         backtracking with memory, only beats 5% in runtime
#         '''
#         from collections import defaultdict
#         visited = defaultdict(int)

#         def bt(v, target):
#             res = 0
#             if v == target:
#                 res += 1
#                 visited[(v, target)] = 1
#             else:
#                 for num in nums:
#                     if num <= target - v:
#                         if (num, target - v) in visited:
#                             res += visited[(num, target - v)]
#                         else:
#                             cnt = bt(num, target - v)
#                             visited[(num, target - v)] = cnt
#                             res += cnt
#             return res

#         counter = 0
#         for num in nums:
#             counter += bt(num, target)

#         return counter


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        dp
        """
        nums.sort()
        dp = [0] * (target + 1)
        for t in range(target + 1):
            for num in nums:
                if num > t:
                    break
                elif num == t:
                    dp[t] += 1
                else:
                    dp[t] += dp[t - num]
        # print(dp)
        return dp[-1]
