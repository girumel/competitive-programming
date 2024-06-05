# Problem: E - Valeriy and Deque - https://codeforces.com/gym/527307/problem/E

from collections import deque

n, q = map(int, input().split())
nums = deque(map(int, input().split()))

pairs = [0] * n
smalls = []
first = nums[0]

for i in range(1, n):
    pairs[i - 1] = (first, nums[i])

    if first > nums[i]:
        smalls.append(nums[i])
    else:
        smalls.append(first)
        first = nums[i]

for _ in range(q):
    m = int(input())
    if m < n:
        print(pairs[m - 1][0], pairs[m - 1][1])
    else:
        m -= n
        print(first, smalls[m % (n - 1)])