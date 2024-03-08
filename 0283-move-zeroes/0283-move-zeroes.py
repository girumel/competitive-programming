class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, h = 0, 0
        while h < len(nums):
            if nums[h] != 0:
                nums[s], nums[h] = nums[h], nums[s]
                s += 1
            h += 1
