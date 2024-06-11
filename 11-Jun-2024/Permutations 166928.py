# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def backtrack(nums, current):
            if not nums:
                permutations.append(current)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], current + [nums[i]])
        
        backtrack(nums, [])
        
        return permutations