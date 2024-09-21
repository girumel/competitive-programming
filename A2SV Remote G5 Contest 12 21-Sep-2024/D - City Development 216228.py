# Problem: D - City Development - https://codeforces.com/gym/520098/problem/D

n = int(input())
m = list(map(int, input().split()))

current = [0] * (n + 1)
optimal = [0] * (n + 1)
max_total = 0

for i in range(1, n + 1):
    current[i] = m[i - 1]
    total = m[i - 1]

    for j in range(i - 1, 0, -1):
        current[j] = min(m[j - 1], current[j + 1])
        total += current[j]

    for j in range(i + 1, n + 1):
        current[j] = min(m[j - 1], current[j - 1])
        total += current[j]

    if total > max_total:
        max_total = total
        optimal = current[1:]

print(*optimal)