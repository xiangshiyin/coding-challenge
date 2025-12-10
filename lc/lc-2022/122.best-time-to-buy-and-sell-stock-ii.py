#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 3 * (10**4) + 1
        high = 0
        profit = 0
        stock = 0
        i = 0
        while i < len(prices):
            if not stock:  # find the next lowest price
                while i < len(prices) and prices[i] <= low:
                    low = min(low, prices[i])
                    i += 1
                if i < len(prices):
                    stock = 1  # buy
                    high = low

            else:  # find the next highest price
                while i < len(prices) and prices[i] >= high:
                    high = max(high, prices[i])
                    i += 1
                if i < len(prices):
                    profit += high - low
                    stock = 0  # sell
                    low = high
        if stock and high > low:
            profit += high - low

        return profit


# @lc code=end
