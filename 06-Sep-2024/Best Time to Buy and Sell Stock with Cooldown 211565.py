# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i == 1:
                dp[i][1] = max(dp[i - 1][1], -prices[i])
            else:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        
        return dp[-1][0]