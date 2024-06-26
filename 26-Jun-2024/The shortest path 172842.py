# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque

n, m = map(int, input().split())
a, b = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)
visited[a] = True

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
queue.append(a)
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            queue.append(v)

if not visited[b]:
    print(-1)
else:
    path = []
    while b != 0:
        path.append(b)
        b = parent[b]
    path.reverse()
    print(len(path) - 1)
    print(" ".join(map(str, path)))