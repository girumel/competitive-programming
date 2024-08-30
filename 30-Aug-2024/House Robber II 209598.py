# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        def helper(start, end):
            rob1, rob2 = 0, 0
            for i in range(start, end):
                new_rob = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        return max(helper(0, n - 1), helper(1, n))