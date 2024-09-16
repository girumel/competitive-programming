# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

n = int(input())
positions = [int(x) * 1000000 for x in input().split()]
speeds = list(map(int, input().split()))

def calc_time(positions, speeds, point):
    max_time = 0
    for pos, speed in zip(positions, speeds):
        max_time = max(max_time, abs(pos - point) / speed)
    return max_time

low = min(positions)
high = max(positions)
min_time = float("inf")

while low <= high:
    mid = (low + high) // 2
    mid_time = calc_time(positions, speeds, mid)
    lower_time = calc_time(positions, speeds, mid - 1)
    higher_time = calc_time(positions, speeds, mid + 1)

    min_time = min(min_time, mid_time, lower_time, higher_time)

    if mid_time < lower_time and mid_time < higher_time:
        break
    elif lower_time > mid_time or mid_time > higher_time:
        low = mid + 1
    else:
        high = mid - 1

print(f"{min_time / 1000000:.12f}")