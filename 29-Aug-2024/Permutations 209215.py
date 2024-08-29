# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(temp, mask):
            if len(temp) == len(nums):
                permutations.append(temp)
                return

            for i in range(len(nums)):
                if mask & 1 << i == 0:
                    backtrack(temp + [nums[i]], mask | 1 << i)
                    
        backtrack([], 0)
        
        return permutations