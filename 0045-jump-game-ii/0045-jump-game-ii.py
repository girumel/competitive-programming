class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        i = nums[0]
        j = nums[0]
        jumps = 1

        for k in range(1, n):
            if j < k:
                jumps += 1
                j = i
            i = max(i, nums[k] + k)

        return jumps