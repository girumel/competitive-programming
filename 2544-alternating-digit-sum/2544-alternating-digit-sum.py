class Solution:
    def alternateDigitSum(self, n: int) -> int:
        nums = str(n)
        i, altsum = 1, 0
        altsum += int(nums[0])
        while i < len(nums):
            if i % 2 == 0:
                altsum += int(nums[i])
            else:
                altsum -= int(nums[i])
            i += 1
        return altsum
    