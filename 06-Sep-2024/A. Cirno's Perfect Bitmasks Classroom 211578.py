# Problem: A. Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    if (x & -x) == x:
        print(x + 1 + (x == 1))
    else:
        print(x & -x)