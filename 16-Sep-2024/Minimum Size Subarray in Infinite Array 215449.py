# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pfx_sum = {0: -1}
        shortest = inf
        
        # current = 0
        # for i in range(2 * n):
        #     current += nums[i % n]
        #     if current - target in pfx_sum:
        #         shortest = min(shortest, i - pfx_sum[current - target])
        #     if i < n:
        #         pfx_sum[current] = i

        # for k in range(1, n + 1):
        #     for i in range(n):
        #         current += nums[i]
        #         if current - target in pfx_sum:
        #             shortest = min(shortest, i + k * n - pfx_sum[current - target])
        #         pfx_sum[current] = i + k * n

        # return shortest if shortest != float('inf') else -1

        window, target = divmod(target, sum(nums))
        if target == 0: 
            return n * window
        
        current = 0
        for i, num in enumerate(2 * nums):
            current += num
            if current - target in pfx_sum:
                shortest = min(shortest, i - pfx_sum[current - target])
            pfx_sum[current] = i

        return (n * window) + shortest if shortest != inf else -1