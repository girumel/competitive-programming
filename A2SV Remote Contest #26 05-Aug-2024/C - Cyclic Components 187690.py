# Problem: C - Cyclic Components - https://codeforces.com/gym/540348/problem/C

from collections import deque

def bfs(u, graph, visited):
    queue = deque([u])
    visited[u] = True
    all_vertices = [u]

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
                all_vertices.append(w)

    return all_vertices

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
count = 0

for i in range(n):
    if not visited[i]:
        all_vertices = bfs(i, graph, visited)
        cyclic = all(len(graph[v]) == 2 for v in all_vertices)
        count += cyclic and len(all_vertices) > 2

print(count)