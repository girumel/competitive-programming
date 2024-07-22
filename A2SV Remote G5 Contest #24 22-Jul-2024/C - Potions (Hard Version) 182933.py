# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

import heapq

n = int(input())
a = list(map(int, input().split()))

heap = []
health = 0
potions = 0

for i in range(n):
    if a[i] + health >= 0:
        health += a[i]
        potions += 1
        if a[i] < 0:
            heapq.heappush(heap, a[i])
    elif heap and a[i] > heap[0]:
        health -= heapq.heappop(heap)
        heapq.heappush(heap, a[i])
        health += a[i]

print(potions)