class Solution:
    def maxProfit(self,prices):
        # Two-pointer approach
        
        left = 0
        max_profit = 0
        
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[right] < prices[left]:
                left = right
        
        return max_profit

            
        