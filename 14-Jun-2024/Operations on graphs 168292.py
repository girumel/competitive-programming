# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

n = int(input())
k = int(input())

graph = {}
for i in range(k):
    s = input().split()
    if s[0] == '1':
        u, v = map(int, s[1:])
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    else:
        u = int(s[1])
        if u in graph:
            print(*graph[u])
        else:
            print()