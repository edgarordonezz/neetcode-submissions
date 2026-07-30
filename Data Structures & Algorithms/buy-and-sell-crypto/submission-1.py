class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)): # iterate through array
            buy_price = prices[i] # get buy price
            for j in range(i + 1, len(prices)): # compute max_profit
                profit = prices[j] - buy_price # calculate profit
                max_profit = max(max_profit, profit) # calculate brute force solution
        return max_profit