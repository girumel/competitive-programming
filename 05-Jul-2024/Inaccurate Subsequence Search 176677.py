# Problem: Inaccurate Subsequence Search - https://codeforces.com/contest/1955/problem/D

import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count_a = defaultdict(int)
    count_b = defaultdict(int)
    count = 0
    result = 0

    for num in b:
        count_b[num] += 1

    for i in range(n):
        count_a[a[i]] += 1

        if count_a[a[i]] <= count_b[a[i]]:
            count += 1

        if i >= m - 1:
            if count >= k:
                result += 1

            count_a[a[i - m + 1]] -= 1

            if count_a[a[i - m + 1]] < count_b[a[i - m + 1]]:
                count -= 1

    print(result)