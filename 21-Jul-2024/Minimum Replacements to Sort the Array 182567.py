# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        threshold = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= threshold:
                threshold = nums[i]
            else:
                needed = math.ceil(nums[i] / threshold)
                count += needed - 1
                threshold = nums[i] // needed
        
        return count