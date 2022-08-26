#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 10 ** 4 + 1
        for p in prices:
            profit = max(profit, p - low)
            low = min(low,p)
        return profit

        
# @lc code=end

