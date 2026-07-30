class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_price = prices[0]

        for price in prices: # iterate through prices
            if min_price > price: # if current minimum price is greater than price
                min_price = min(min_price, price) # set min price to smallest price
            profit = price - min_price # calculate profit
            max_profit = max(max_profit, profit) # get maximum profit
        return max_profit 