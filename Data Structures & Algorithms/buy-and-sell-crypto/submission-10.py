class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum profit = Price of NeetCoin is less - max sale
        maximum = 0
        l = 0
        # 10 , 1, ...
        # l    i
        # is 10 < 1? no, so increment l
        # is 1 < 5? yes, keep l there and continue with i
        for i in range(1, len(prices)):
            while prices[l] > prices[i]:
                l += 1
            maximum = max(maximum, (prices[i] - prices[l]))

        return maximum
