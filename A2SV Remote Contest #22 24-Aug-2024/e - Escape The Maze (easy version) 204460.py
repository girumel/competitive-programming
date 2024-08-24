# Problem: e - Escape The Maze (easy version) - https://codeforces.com/gym/533316/problem/e

from collections import deque

t = int(input())

for _ in range(t):
    _ = input()
    n, k = map(int, input().split())
    color = [0] * (n + 1)
    color[1] = 1
    queue = deque()
    friends = list(map(int, input().split()))

    for friend in friends:
        color[friend] = 2
        queue.append((friend, 2))
    queue.append((1, 1))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    while queue:
        x, y = queue.popleft()
        if y == 1 and x != 1 and len(adj[x]) == 1:
            # print(*[x, y, adj[x][0]])
            print("YES")
            break
        for u in adj[x]:
            if color[u] == 0:
                color[u] = y
                queue.append((u, y))
    else:
        print("NO")