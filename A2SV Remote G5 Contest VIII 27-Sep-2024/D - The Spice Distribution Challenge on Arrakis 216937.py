# Problem: D - The Spice Distribution Challenge on Arrakis - https://codeforces.com/gym/514056/problem/D

n, m = map(int, input().split())
spices = list(map(int, input().split()))

current = 0
counts = {0: 1}
pairs = 0

for spice in spices:
    current += spice
    remainder = current % m
    if remainder in counts:
        pairs += counts[remainder]
        counts[remainder] += 1
    else:
        counts[remainder] = 1

print(pairs)