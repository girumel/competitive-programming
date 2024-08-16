# Problem: E - World is Mine - https://codeforces.com/gym/536373/problem/E

import heapq
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    counts = list(Counter(values).items())

    counts.sort()
    max_heap = []

    cakes = 0
    for i in range(len(counts)):
        tastiness, count = counts[i]
        cakes += count
        heapq.heappush(max_heap, (-count, tastiness))

        if i - len(max_heap) + 1 < cakes:
            cakes += heapq.heappop(max_heap)[0]

    print(len(counts) - len(max_heap))