class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > 0:
                maxProfit = max(profit,maxProfit)
            else:
                buy = sell
        return maxProfit