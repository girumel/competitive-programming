# Problem: C - Operation 2 - https://codeforces.com/gym/521860/problem/C

from collections import deque

a, b = map(int, input().split())

queue = deque([(a, 0)])
visited = set([a])

while queue:
    cur, ops = queue.popleft()
    if cur == b:
        print(ops)
        break
    if cur * 2 <= b * 2 and cur * 2 not in visited:
        queue.append((cur * 2, ops + 1))
        visited.add(cur * 2)
    if cur - 1 >= 0 and cur - 1 not in visited:
        queue.append((cur - 1, ops + 1))
        visited.add(cur - 1)
else:
    print(-1)