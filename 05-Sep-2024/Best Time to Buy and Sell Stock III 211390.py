# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1 = [0] * n
        dp2 = [0] * n
        
        min_price = prices[0]
        max_price = prices[-1]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp1[i] = max(dp1[i-1], prices[i] - min_price)
        
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            dp2[i] = max(dp2[i+1], max_price - prices[i] + dp1[i])
        
        return dp2[0]