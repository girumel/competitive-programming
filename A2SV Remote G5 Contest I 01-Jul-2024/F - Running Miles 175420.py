# Problem: F - Running Miles - https://codeforces.com/gym/500425/problem/F

t = int(input())

for _ in range(t):
    n = int(input())
    beauties = list(map(int, input().split()))

    prefix = [0] * (n + 2)
    suffix = [0] * (n + 2)
    prefix[0] = 0
    suffix[n + 1] = float("-inf")

    for i in range(n):
        prefix[i + 1] = max(prefix[i], beauties[i] + i)

    for i in range(n - 1, -1, -1):
        suffix[i + 1] = max(suffix[i + 2], beauties[i] - i)

    max_beauty = 0
    for i in range(1, n - 1):
        max_beauty = max(max_beauty, prefix[i] + suffix[i + 2] + beauties[i])

    print(max_beauty)