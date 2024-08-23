# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
                    elif dp[i] == dp[j]+1:
                        count[i] += count[j]

        max_len = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == max_len:
                ans += count[i]
            #else:
            #   ans += count[i]
        
        return ans