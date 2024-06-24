# Problem: C - Mahmoud and Ehab and the bipartiteness - https://codeforces.com/gym/531416/problem/C

import sys, threading

def main():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    colors = [0, 0]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node, parent, color):
        colors[color] += 1
        for child in adj[node]:
            if child != parent:
                dfs(child, node, 1 - color)

    dfs(1, 0, 0)

    print(colors[0] * colors[1] - (n - 1))

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

thread = threading.Thread(target=main)
thread.start()
thread.join()