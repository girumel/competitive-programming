# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def backtrack(remaining, current, start):
            if remaining == 0:
                combinations.append(list(current))
                return
            if remaining <= 0:
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(remaining - candidates[i], current, i)
                current.pop()
        
        backtrack(target, [], 0)
        
        return combinations