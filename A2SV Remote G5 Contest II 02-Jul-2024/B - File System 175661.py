# Problem: B - File System - https://codeforces.com/gym/504384/problem/B

n = int(input())
fs = set()
last = {}
for i in range(n):
    name = input()
    if name not in fs:
        fs.add(name)
        last[name] = 0
        print("OK")
    else:
        last[name] += 1
        new_name = name + str(last[name])
        fs.add(new_name)
        last[new_name] = 0
        print(new_name)
