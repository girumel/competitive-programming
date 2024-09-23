# Problem: C - Array Difference - https://codeforces.com/gym/518838/problem/C

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)
    diff = 0
    switch = -1

    # for i in range(n):
    #     diff += abs(a[i] - b[i])

    for i in range(n):
        if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
            switch = i
            break
        diff += abs(a[i] - b[i])

    if switch != -1:
        for i in range(switch, n):
            diff += abs(a[i] - b[-(n - i)])
    print(diff)