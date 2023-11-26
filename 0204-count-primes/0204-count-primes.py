class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primes = [True for i in range(n)]
        primes[0] = primes[1] = False
        
        p = 2
        while (p*p <= n):
            if primes[p] == True:
                for x in range(p*p, n, p):
                    primes[x] = False
            p += 1
        
        return primes.count(True)
    