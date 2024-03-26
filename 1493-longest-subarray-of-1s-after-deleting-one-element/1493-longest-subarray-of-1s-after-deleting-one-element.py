class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        zeros = 0
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            longest = max(longest, right - left)
            right += 1

        return longest
    