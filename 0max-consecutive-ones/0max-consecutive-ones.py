class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones, ones = 0, 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                ones = 0
            max_ones = max(ones, max_ones)
        return max_ones
                