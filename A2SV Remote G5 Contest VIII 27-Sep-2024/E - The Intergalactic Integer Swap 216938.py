# Problem: E - The Intergalactic Integer Swap - https://codeforces.com/gym/514056/problem/E

from math import gcd

n = int(input())
coordinates = list(map(int, input().split()))

prefix_gcd = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_gcd[i] = gcd(prefix_gcd[i - 1], coordinates[i - 1])

suffix_gcd = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i + 1], coordinates[i])

max_gcd = 0
for i in range(n):
    max_gcd = max(max_gcd, gcd(prefix_gcd[i], suffix_gcd[i + 1]))

print(max_gcd)