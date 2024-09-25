# Problem: D - Swap Letters - https://codeforces.com/gym/515369/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    
    ops = 0
    swapped = set()

    for i in range(n - 1, -1, -1):
        if s[i] == "A":
            j = i
            while j + 1 < n and s[j + 1] == "B" and j not in swapped:
                # s = s[:j] + "B" + "A" + s[j + 2 :]
                s[j], s[j + 1] = s[j + 1], s[j]
                ops += 1
                swapped.add(j)
                j += 1
    print(ops)