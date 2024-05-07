# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = 0
        min_values = []
        max_values = []

        for right in range(n):
            while min_values and nums[right] < min_values[-1]:
                min_values.pop()
            min_values.append(nums[right])
            
            while max_values and nums[right] > max_values[-1]:
                max_values.pop()
            max_values.append(nums[right])

            if max_values[0] - min_values[0] > limit:
                if min_values[0] == nums[left]:
                    min_values.pop(0)
                if max_values[0] == nums[left]:
                    max_values.pop(0)
                left += 1

        return right - left + 1