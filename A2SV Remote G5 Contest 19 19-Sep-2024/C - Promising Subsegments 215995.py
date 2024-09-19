# Problem: C - Promising Subsegments - https://codeforces.com/gym/529269/problem/C

import sys
import random
from collections import Counter

input = sys.stdin.readline
key = random.randint(1, 10**9)

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_count = Counter()
    b_count = Counter(bi ^ key for bi in b)
    matching = 0
    promising = 0

    left = 0
    for right in range(n):
        a_count[a[right] ^ key] += 1
        if a_count[a[right] ^ key] <= b_count[a[right] ^ key]:
            matching += 1

        if right >= m:
            if a_count[a[left] ^ key] <= b_count[a[left] ^ key]:
                matching -= 1
            a_count[a[left] ^ key] -= 1
            left += 1

        if right - left + 1 == m and matching >= k:
            promising += 1

    print(promising)