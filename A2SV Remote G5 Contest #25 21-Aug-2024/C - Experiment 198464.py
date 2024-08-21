# Problem: C - Experiment - https://codeforces.com/gym/537575/problem/C

n = int(input())

experiments = []
for _ in range(n):
    s, t, b = map(int, input().split())
    experiments.append((s, t, b))

max_time = 10004
room_changes = [0] * (max_time + 1)

for si, ti, bi in experiments:
    room_changes[si] += bi
    room_changes[ti + 1] -= bi

max_rooms = 0
current_rooms = 0
for change in room_changes:
    current_rooms += change
    if current_rooms > max_rooms:
        max_rooms = current_rooms

print(max_rooms)