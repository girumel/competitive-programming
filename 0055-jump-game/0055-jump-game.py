class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = 0
        i = 0
        while i < n and i <= max_jump:
            max_jump = max(max_jump, nums[i] + i)
            i += 1
            
        if max_jump >= n - 1:
            return True
        else:
            return False