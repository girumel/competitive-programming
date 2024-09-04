# Problem: C - Tournament - https://codeforces.com/gym/544347/problem/C

from math import log2

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    # max_halves = int(log2(max(p))) + 1
    max_halves = max(p).bit_length() + 1
    dp = [[0] * (max_halves + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for h in range(max_halves):
            # remaining = p[i] >> h
            remaining = p[i] // (2 ** h)
            full_pick = remaining - k + dp[i + 1][h]
            half_pick = (remaining // 2) + dp[i + 1][h + 1]
            dp[i][h] = max(full_pick, half_pick)

    print(dp[0][0])