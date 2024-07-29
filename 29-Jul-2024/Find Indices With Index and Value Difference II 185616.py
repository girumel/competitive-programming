# Problem: Find Indices With Index and Value Difference II - https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_index = max_index = 0
        
        for i in range(indexDifference, len(nums)):
            current = i - indexDifference

            if nums[current] > nums[max_index]:
                max_index = current
            if nums[current] < nums[min_index]:
                min_index = current
            if nums[i] - nums[min_index] >= valueDifference:
                return [min_index, i]
            if nums[max_index] - nums[i] >= valueDifference:
                return [max_index, i]
        return [-1, -1]