class Solution:
    """
    Best Time to Buy and Sell Stock
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    
    """
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        j = n-1
        i = n-2
        max_profit = 0

        while i >= 0:
            x = prices[i]
            y = prices[j]
            profit = y - x

            if profit > max_profit:
                max_profit = profit

            if x > y:
                i-=1
                j-=1
            else:
                prices[i] = prices[j]
                j-=1
                i-=1
        
        return max_profit  