class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # exceptions
        if prices is None:
            return None
        N = len(prices)
        if N<=1:
            return 0
        
        # traverse the list
        max_profit = 0
        buy = prices[0]
        for idx in range(1,N):
            max_profit = max(prices[idx]-buy, max_profit)
            if prices[idx] < buy:
                buy = prices[idx]
                
                
        return max_profit
        