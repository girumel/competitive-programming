# Problem: B - Algorithm Test II - https://codeforces.com/gym/544347/problem/B

# Based on Nahom's approach

from collections import defaultdict, deque, Counter

positions = defaultdict(deque)
counts = Counter()
graph = defaultdict(list)
pending = []
removed = set()

q = int(input())
for _ in range(q):
    query = input().split()
    if query[0] == "insert":
        _, x, y = query
        if y in positions and positions[y]:
            graph[positions[y][0]].append((x, counts[x]))
        else:
            pending.append((x, counts[x]))
        
        positions[x].append((x, counts[x]))
        counts[x] += 1

    elif query[0] == "remove":
        _, w = query
        if w in positions and positions[w]:
            removed.add(positions[w].popleft())

result = []
def dfs(node):
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in removed:
            result.append(node[0])
        for neighbor in graph[node]:
            stack.append(neighbor)

for val in pending:
    dfs(val)

print(' '.join(result))