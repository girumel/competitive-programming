# Problem: C - Little Girl and Maximum Sum - https://codeforces.com/gym/514056/problem/C

n, q = map(int, input().split())
array = list(map(int, input().split()))
queries = []
for _ in range(q):
    queries.append(tuple(map(int, input().split())))

freq = [0] * (n + 1)

for x, y in queries:
    freq[x - 1] += 1
    if y < n:
        freq[y] -= 1

for i in range(1, n):
    freq[i] += freq[i - 1]

array.sort(reverse=True)
freq.sort(reverse=True)

max_sum = 0
for a, f in zip(array, freq):
    max_sum += a * f

print(max_sum)