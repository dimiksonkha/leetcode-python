class Solution:
    """
    Best Time to Buy and Sell Stock II
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    
    """
    def get_max_price(self, prices):
        max_price = prices[0]
        for price in prices:
            if price > max_price :
                max_price = price
        return max_price
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        purchase_indices = []
        max_profit = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                purchase_indices.append(i)
                
        m = len(purchase_indices)
        for j in range(m):
            if j+1 == m:
                end_index = n
            else:    
                end_index = purchase_indices[j+1]+1
            max_price = self.get_max_price(prices[purchase_indices[j]+1:end_index])
            profit = max_price - prices[purchase_indices[j]]
            max_profit+=profit
            
        return max_profit