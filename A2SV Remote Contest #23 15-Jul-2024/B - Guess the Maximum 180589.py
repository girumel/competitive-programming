# Problem: B - Guess the Maximum - https://codeforces.com/gym/535309/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_k = float("inf")
    for i in range(1, n):
        max_k = min(max_k, max(a[i - 1], a[i]))

    print(max_k - 1)