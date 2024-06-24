# Problem: B - Network Topology - https://codeforces.com/gym/531416/problem/B

n, m = map(int, input().split())
c = {}

for _ in range(m):
    a, b = map(int, input().split())
    c[a] = c.get(a, 0) + 1
    c[b] = c.get(b, 0) + 1

t = [0, 0, 0]
for key in c.values():
    if key == 1:
        t[1] += 1
    elif key == 2:
        t[2] += 1
    else:
        t[0] += 1

if t[1] == 2 and t[0] == 0:
    print("bus topology")
elif t[1] == 0 and t[0] == 0:
    print("ring topology")
elif t[1] == n - 1 and t[2] == 0 and t[0] == 1:
    print("star topology")
else:
    print("unknown topology")