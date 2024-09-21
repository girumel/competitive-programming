# Problem: D - Maximum Median - https://codeforces.com/gym/523225/problem/D

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
max_median = a[n // 2]

low, high = 1, 2 * 10**9
while low <= high:
    mid = (low + high) // 2
    sum_needed = sum(max(0, mid - a[i]) for i in range(n // 2, n))

    if sum_needed <= k:
        max_median = max(max_median, mid)
        low = mid + 1
    else:
        high = mid - 1

print(max_median)