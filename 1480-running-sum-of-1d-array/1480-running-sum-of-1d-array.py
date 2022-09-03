class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for n in range(1, len(nums)):
            nums[n] += nums[n - 1]
            n += 1
        return nums