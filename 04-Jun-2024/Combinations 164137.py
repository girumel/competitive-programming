# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []
        combinations = []

        def backtrack(start):
            if len(current) == k:
                combinations.append(current[:])
                return

            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1)
                current.pop()

        backtrack(1)
        
        return combinations