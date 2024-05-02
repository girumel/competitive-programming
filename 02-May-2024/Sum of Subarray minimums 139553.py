# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = [0] * n, [0] * n

        stack = []
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))

        stack = []
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))

        result = 0
        for i in range(n):
            result += arr[i] * left[i] * right[i]
        
        return result % (10**9 + 7)