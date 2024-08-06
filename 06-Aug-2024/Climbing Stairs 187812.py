# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)

        def helper(n, memo):
            if n <= 2:
                return n
            if memo[n] != -1:
                return memo[n]
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
            return memo[n]
        
        return helper(n, memo)