# Problem: D - Sum - https://codeforces.com/gym/510902/problem/D

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    elements = list(map(int, input().split()))

    elements.sort()

    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + elements[i]

    max_sum = 0
    for i in range(k + 1):
        cur_sum = ps[n - i] - ps[2 * (k - i)]
        max_sum = max(max_sum, cur_sum)

    print(max_sum)