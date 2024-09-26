# Problem: D - A Game of Numbers - https://codeforces.com/gym/508510/problem/D

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    frodo = sorted(map(int, input().split()))
    sam = sorted(map(int, input().split()))

    frodo_l, frodo_r = 0, n - 1
    sam_l, sam_r = 0, m - 1
    max_diff = 0

    while frodo_l <= frodo_r:
        diff_l = abs(frodo[frodo_l] - sam[sam_r])
        diff_r = abs(frodo[frodo_r] - sam[sam_l])

        if diff_l >= diff_r:
            max_diff += diff_l
            frodo_l += 1
            sam_r -= 1
        else:
            max_diff += diff_r
            frodo_r -= 1
            sam_l += 1

    print(max_diff)