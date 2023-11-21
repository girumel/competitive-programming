class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        k = 0
        shuffled = [0] * len(nums)
        while i < n and j < len(nums):
            shuffled[k] = nums[i]
            shuffled[k+1] = nums[j]
            i += 1
            j += 1
            k += 2
        return shuffled
