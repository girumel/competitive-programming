class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for num in nums:
            if nums.count(target):
                return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)        