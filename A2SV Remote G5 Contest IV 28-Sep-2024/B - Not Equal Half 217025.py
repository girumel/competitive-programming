# Problem: B - Not Equal Half - https://codeforces.com/gym/507024/problem/B

n = int(input())
a = list(map(int, input().split()))

a.sort()

first_half = sum(a[:n])
last_half = sum(a[n:])

if first_half == last_half:
    print(-1)
else:
    print(*a)