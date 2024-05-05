# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = 10**9 + 7

        def fast_expo(base, exp):
            if exp == 0:
                return 1
            elif exp % 2 == 0:
                half = fast_expo(base, exp // 2)
                return (half * half) % modulo
            else:
                half = fast_expo(base, exp // 2)
                return (base * half * half) % modulo

        return (fast_expo(5, (n + 1) // 2) * fast_expo(4, n // 2)) % modulo