class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        from bisect import bisect_left

        # sort the envelopes
        envelopes.sort(key=lambda x: (x[0], -1 * x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                ix = bisect_left(dp, nums[i])
                if ix == len(dp):
                    dp.append(nums[i])
                else:
                    dp[ix] = nums[i]
            return len(dp)

        return lis([env[1] for env in envelopes])
