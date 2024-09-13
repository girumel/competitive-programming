# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())

recipes = []
for _ in range(n):
    l, r = map(int, input().split())
    recipes.append((l, r))

queries = []
for _ in range(q):
    a, b = map(int, input().split())
    queries.append((a, b))

max_temp = 200000
temp = [0] * (max_temp + 1)
for l, r in recipes:
    temp[l] += 1
    if r + 1 <= max_temp:
        temp[r + 1] -= 1

current = 0
admissible = [0] * (max_temp + 1)
for i in range(1, max_temp + 1):
    current += temp[i]
    if current >= k:
        admissible[i] = 1

for i in range(1, max_temp + 1):
    admissible[i] += admissible[i - 1]

results = []
for a, b in queries:
    results.append(admissible[b] - admissible[a - 1])

print("\n".join(map(str, results)))