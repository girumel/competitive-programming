class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0

        for num in nums:
            ones = ones + 1 if num == 1 else 0
            max_ones = max(ones, max_ones)

        return max_ones
