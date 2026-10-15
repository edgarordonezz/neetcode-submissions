class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            profit = 0
            buy = min(buy, prices[i])
            profit = prices[i] - buy
            maxProfit = max(maxProfit, profit)
        return maxProfit
            