# Problem: D - Firaol With His Game - https://codeforces.com/gym/545837/problem/D

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    times = list(map(int, input().split()))

    if sum(times) <= s:
        print(0)
        continue

    total_time = 0
    max_time = 0
    skip_index = 0

    for i in range(n):
        total_time += times[i]
        if times[i] > max_time:
            max_time = times[i]
            skip_index = i + 1
        if total_time > s:
            break

    if total_time - max_time <= s:
        print(skip_index)
    else:
        print(0)