# Problem: A - Perfect Rectangle - https://codeforces.com/gym/529269/problem/A

from math import isqrt

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    if isqrt(total) ** 2 == total:
        print("YES")
    else:
        print("NO")