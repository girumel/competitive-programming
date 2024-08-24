# Problem: d - Valid BFS? - https://codeforces.com/gym/533316/problem/d

from collections import deque

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

a = list(map(int, input().split()))
index = [0] * (n + 1)
for i in range(n):
    index[a[i]] = i

def bfs(adj):
    order = []
    queue = deque()
    visited = [False] * (len(adj) + 1)
    visited[1] = True
    queue.append(1)

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return order

for i in range(1, n + 1):
    adj[i].sort(key=lambda x: index[x])

if bfs(adj) == a:
    print("Yes")
else:
    print("No")