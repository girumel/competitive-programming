class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left = 0
        shortest = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                total -= nums[left]
                shortest = min(shortest, right - left + 1)
                left += 1

        if shortest == float('inf'):
            return 0
        else:
            return shortest