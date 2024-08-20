# Problem: D - Rudolf and k Bridges - https://codeforces.com/gym/543262/problem/D

from collections import deque

def calc(depths, m, d):
    queue = deque([(0, 1)]) # (index, cost)
    for i in range(1, m):
        while queue and i - queue[0][0] - 1 > d:
            queue.popleft()
        cost = queue[0][1] + depths[i] + 1
        while queue and queue[-1][1] >= cost:
            queue.pop()
        queue.append((i, cost))
    return queue[-1][1]

t = int(input())
for _ in range(t):
    n, m, k, d = map(int, input().split())
    depths = []
    for _ in range(n):
        depths.append(list(map(int, input().split())))
    pfx_sum = [0]
    min_cost = float("inf")
    for i in range(n):
        pfx_sum.append(pfx_sum[-1] + calc(depths[i], m, d))
        if i + 1 >= k:
            last_sum = pfx_sum[-1] - pfx_sum[i - k + 1]
            min_cost = min(min_cost, last_sum)
    
    print(min_cost)