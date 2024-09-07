# Problem: B - Rehearsal - https://codeforces.com/gym/523225/problem/B

t = int(input())
musicians = []
for _ in range(t):
    musicians.append(list(map(int, input().split())))

musicians.sort(key=lambda x: x[1])

left, right = 0, len(musicians) - 1
min_time = float("-inf")

while left <= right:
    min_time = max(min_time, musicians[left][1] + musicians[right][1])
    min_count = min(musicians[left][0], musicians[right][0])

    if left == right:
        break

    musicians[left][0] -= min_count
    musicians[right][0] -= min_count

    if musicians[left][0] == 0:
        left += 1
    if musicians[right][0] == 0:
        right -= 1

print(min_time)