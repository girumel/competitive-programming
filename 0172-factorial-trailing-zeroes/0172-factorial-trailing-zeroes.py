class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        fac = str(factorial(n))
        while fac[-1] == '0':
            fac = fac[:-1]
            zeros += 1
        return zeros
    
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)