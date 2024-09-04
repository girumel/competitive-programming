# Problem: D - Maximize the Root - https://codeforces.com/gym/544347/problem/D

from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))

    tree = defaultdict(list)
    for i in range(1, n):
        tree[p[i-1] - 1].append(i + 1)

    stack = [(1, False)]
    max_vals = [0] * (n + 1)
    while stack:
        node, visited = stack.pop()
        if visited:
            if not tree[node - 1]:
                max_vals[node] = a[node - 1]
            else:
                min_child = min(max_vals[child] for child in tree[node - 1])
                if node == 1:
                    max_vals[node] = a[node - 1] + min_child
                else:
                    max_vals[node] = min((a[node - 1] + min_child) // 2, min_child)
        else:
            stack.append((node, True))
            stack.extend((child, False) for child in tree[node - 1])

    print(max_vals[1])