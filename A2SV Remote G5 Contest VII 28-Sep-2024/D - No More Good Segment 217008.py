# Problem: D - No More Good Segment - https://codeforces.com/gym/511771/problem/D

n, s = map(int, input().split())
sizes = sorted(int(input()) for _ in range(n))

intervals = [0] * n
max_intervals = [0] * (n + 1)
max_intervals[0] = intervals[0]
left = 0

for right in range(n):
    while sizes[right] - sizes[left] > s:
        left += 1
    intervals[right] = right - left + 1

for i in range(1, n):
    max_intervals[i] = max(intervals[i], max_intervals[i - 1])

max_stones = 0
for i in range(n):
    # if i >= intervals[i]:
    #     max_stones = max(max_stones, intervals[i] + max_intervals[i - intervals[i]])
    current = intervals[i] + max_intervals[i - intervals[i]]
    max_stones = max(max_stones, current)

print(max_stones)