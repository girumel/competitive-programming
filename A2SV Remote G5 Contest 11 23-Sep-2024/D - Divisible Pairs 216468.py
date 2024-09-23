# Problem: D - Divisible Pairs - https://codeforces.com/gym/518838/problem/D

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    array = list(map(int, input().split()))
    
    mods = {}
    count = 0
    
    for idx, a in enumerate(array):
        key = ((x - (a % x)) % x, a % y)
        if key in mods:
            count += len(mods[key])
        mod_key = (a % x, a % y)
        if mod_key not in mods:
            mods[mod_key] = set()
        mods[mod_key].add(idx)

    print(count)