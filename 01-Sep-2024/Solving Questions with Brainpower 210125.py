# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [-1] * n
        
        def dp(index):
            if index >= n:
                return 0
            if memo[index] != -1:
                return memo[index]
            
            points, bonus = questions[index]
            solve = points + dp(index + bonus + 1)
            skip = dp(index + 1)
            
            memo[index] = max(solve, skip)
            return memo[index]
        
        return dp(0)