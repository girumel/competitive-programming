# Problem: D - Quadruplet - https://codeforces.com/gym/504384/problem/D

n, target = map(int, input().split())
a = list(map(int, input().split()))

pair_sums = {}

for i in range(n):
    for j in range(i + 1, n):
        current = a[i] + a[j]
        if target - current in pair_sums:
            a_idx, b_idx = pair_sums[target - current]
            print(a_idx, b_idx, i + 1, j + 1)
            exit()
    for j in range(i):
        pair_sums[a[i] + a[j]] = (j + 1, i + 1)

print("IMPOSSIBLE")