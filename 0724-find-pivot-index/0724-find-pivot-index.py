class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        left_sum = 0
        right_sum = sum(nums)

        for i in range(n):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1