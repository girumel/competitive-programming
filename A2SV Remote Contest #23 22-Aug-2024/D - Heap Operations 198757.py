# Problem: D - Heap Operations - https://codeforces.com/gym/535309/problem/D

import heapq

n = int(input().strip())
operations = []
heap = []
heapq.heapify(heap)
count = 0

for _ in range(n):
    line = input().strip().split()
    cmd = line[0]
    if cmd == "insert":
        x = int(line[1])
        heapq.heappush(heap, x)
        operations.append((cmd, x))
    elif cmd == "getMin":
        x = int(line[1])
        while heap and heap[0] < x:
            heapq.heappop(heap)
            operations.append(("removeMin",))
            count += 1
        if not heap or heap[0] > x:
            heapq.heappush(heap, x)
            operations.append(("insert", x))
            count += 1
        operations.append((cmd, x))
    elif cmd == "removeMin":
        if not heap:
            operations.append(("insert", 1))
            count += 1
        else:
            heapq.heappop(heap)
        operations.append((cmd,))

print(len(operations))
for op in operations:
    if len(op) == 1:
        print(op[0])
    else:
        print(op[0], op[1])