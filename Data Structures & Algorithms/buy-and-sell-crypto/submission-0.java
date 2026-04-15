class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int min = prices[0];

        for (int price : prices) {
            // profit = compare profit with 7 - current minimumso 
            profit = Math.max(profit, price - min);
            // update minimum
            min = Math.min(min, price);
        }
        return profit;
    }
}
