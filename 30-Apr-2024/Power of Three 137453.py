# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        else:
            return self.isPowerOfThree(n / 3)