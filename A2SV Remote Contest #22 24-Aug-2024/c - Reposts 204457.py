# Problem: c - Reposts - https://codeforces.com/gym/533316/problem/c

n = int(input())
reposts = {}
reposts["polycarp"] = 1
max_length = 1
for _ in range(n):
    a, _, b = input().lower().split()
    reposts[a] = reposts.get(b, 0) + 1
    max_length = max(max_length, reposts[a])

print(max_length)