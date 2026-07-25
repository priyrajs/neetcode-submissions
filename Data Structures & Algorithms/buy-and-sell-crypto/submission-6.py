class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        buy = 0

        for sell in range(1, len(prices)):
            if prices[sell] - prices[buy] > maxx:
                maxx = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell

        return maxx