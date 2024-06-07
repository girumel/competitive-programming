# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(subset, start):
            if len(nums) == start:
                subsets.append(subset[:])
                return
            
            backtrack(subset, start+1) # Exclude current element 
            backtrack(subset + [nums[start]], start+1) # Include current element

        backtrack(subset=[], start=0)

        return subsets