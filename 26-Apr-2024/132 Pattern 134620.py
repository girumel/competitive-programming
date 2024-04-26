# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_val = float('-inf')

        for num in reversed(nums):
            if num < min_val:
                return True
            
            while stack and stack[-1] < num:
                min_val = stack.pop()
            stack.append(num)

        return False