# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n = list(map(int, input().split()))
a = list(map(int, input().split()))

i = 1
while i < n[1]:
    i += a[i - 1]
    if i == n[1]:
        print("YES")
        break
    if i > n[1]:
        print("NO")
        break
else:
    print("NO")