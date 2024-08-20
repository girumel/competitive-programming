# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        
        for num in nums:
            new_dp = {}
            for s, count in dp.items():
                new_dp[s + num] = new_dp.get(s + num, 0) + count
                new_dp[s - num] = new_dp.get(s - num, 0) + count
            dp = new_dp
            
        return dp.get(target, 0)