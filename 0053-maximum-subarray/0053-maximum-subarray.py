class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        local_max = global_max = nums[0]
        
        for i in range(1, n):
            if nums[i] > local_max + nums[i]:
                local_max = nums[i]
            else:
                local_max += nums[i]

            if local_max > global_max:
                global_max = local_max
        
        return global_max