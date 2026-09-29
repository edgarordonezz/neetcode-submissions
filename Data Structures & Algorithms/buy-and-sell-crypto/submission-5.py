class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # trick is to find the lowest and subtract with all the other prices, I think
        lowest = prices[0]
        mxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            mxProfit = max(mxProfit, prices[i] - lowest)
            


            
        return mxProfit
           

