# Problem: E - Maximum White Subtree - https://codeforces.com/gym/544347/problem/E

import sys
import threading
from collections import defaultdict

def calc_sub_diff(node, parent):
    for neighbor in adj[node]:
        if neighbor != parent:
            calc_sub_diff(neighbor, node)
            sub_diff[node] += max(sub_diff[neighbor], 0)
    sub_diff[node] += colors[node]

def calc_max_diff(node, parent, value):
    max_diff[node] = sub_diff[node] + value
    for neighbor in adj[node]:
        if neighbor != parent:
            diff = max(max_diff[node] - max(sub_diff[neighbor], 0), 0)
            calc_max_diff(neighbor, node, diff)

def main():
    n = int(input())
    global colors, adj, sub_diff, max_diff
    colors = list(map(lambda x: int(x) if int(x) == 1 else -1, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    
    adj = defaultdict(list)
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    sub_diff = [0] * n
    max_diff = [float("inf")] * n

    calc_sub_diff(0, -1)
    calc_max_diff(0, -1, 0)

    print(" ".join(map(str, max_diff)))

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()