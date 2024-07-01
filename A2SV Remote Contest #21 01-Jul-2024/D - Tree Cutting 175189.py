# Problem: D - Tree Cutting - https://codeforces.com/gym/532332/problem/D

import sys, threading
from collections import defaultdict

input = sys.stdin.readline

def main():
    t = int(input())

    def dfs(node, parent, x):
        nonlocal count
        sizes[node] = 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node, x)
            sizes[node] += sizes[neighbor]
        if sizes[node] >= x and count < k:
            count += 1
            sizes[node] = 0

    results = []
    for _ in range(t):
        n, k = map(int, input().split())
        adj = defaultdict(list)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        x = 0
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            sizes = [0] * (n + 1)
            count = 0
            dfs(1, -1, mid)
            if count >= k and sizes[1] >= mid:
                x = max(x, mid)
                left = mid + 1
            else:
                right = mid - 1
        results.append(x)

    for result in results:
        print(result)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

thread = threading.Thread(target=main)
thread.start()
thread.join()