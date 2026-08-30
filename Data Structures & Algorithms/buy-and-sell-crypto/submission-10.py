class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > maxProfit:
                maxProfit = profit
            elif prices[buy] > prices[sell]:
                buy = sell
        return maxProfit