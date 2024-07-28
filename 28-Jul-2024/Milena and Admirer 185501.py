# Problem: Milena and Admirer - https://codeforces.com/problemset/problem/1898/B

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    min_ops = 0

    for i in range(n - 2, -1, -1):
        x = (a[i] + a[i + 1] - 1) // a[i + 1]
        min_ops += x - 1
        a[i] //= x

    print(min_ops)
