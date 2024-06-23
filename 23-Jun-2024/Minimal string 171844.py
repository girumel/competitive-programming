# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

s = input()

t = []
u = []
i = 0

for c in map(chr, range(ord("a"), ord("z") + 1)):
    while t and t[-1] <= c:
        u.append(t.pop())

    pos = s.find(c, i)
    while pos >= 0:
        t.extend(s[i:pos])
        i = pos + 1
        u.append(c)
        pos = s.find(c, i)

u.extend(reversed(t))

print("".join(u))