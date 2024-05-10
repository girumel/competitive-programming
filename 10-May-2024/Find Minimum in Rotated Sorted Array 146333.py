# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid

        return nums[left]