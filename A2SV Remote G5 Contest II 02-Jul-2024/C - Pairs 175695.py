# Problem: C - Pairs - https://codeforces.com/gym/504384/problem/C

from collections import Counter

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

count_a = Counter(a)
count_c = Counter(c)

pairs = sum(count_a[num] * count_c[idx + 1] for idx, num in enumerate(b))

print(pairs)