# Problem: D - Xor-tree - https://codeforces.com/gym/531416/problem/D

import sys, threading

def main():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    ops = []

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    init = list(map(int, input().split()))
    goal = list(map(int, input().split()))

    for i in range(1, n + 1):
        visited[i] = goal[i - 1] != init[i - 1]

    def dfs(node, parent, depth, odd, even):
        flip = False
        if depth % 2 == 1:
            if (visited[node] + odd) % 2:
                ops.append(node)
                flip = True
        else:
            if (visited[node] + even) % 2:
                ops.append(node)
                flip = True

        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if not flip:
                dfs(neighbor, node, depth + 1, odd, even)
                continue
            if depth % 2 == 1:
                dfs(neighbor, node, depth + 1, odd + 1, even)
            else:
                dfs(neighbor, node, depth + 1, odd, even + 1)

    dfs(1, 0, 0, 0, 0)

    print(len(ops))
    for op in ops:
        print(op)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()