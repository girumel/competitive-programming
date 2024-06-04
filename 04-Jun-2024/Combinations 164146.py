# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(start, current):
            # Base case: combination of size k is found
            if len(current) == k:
                combinations.append(current[:])
                return

            # Recursive case: explore all possible choices
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)  # Explore next number
                current.pop()  # Backtrack by removing the last number

        backtrack(1, [])
        return combinations