# Problem: C - Kenenisa's Dilemma - https://codeforces.com/gym/507024/problem/C

n = int(input())
a = list(map(int, input().split()))

swaps = []

for i in range(n):
    min_index = min(range(i, n), key=a.__getitem__)
    if min_index != i:
        swaps.append((i, min_index))
        a[i], a[min_index] = a[min_index], a[i]

print(len(swaps))
for i, j in swaps:
    print(i, j)