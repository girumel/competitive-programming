# Problem: D - Dreamoon and WiFi - https://codeforces.com/gym/521860/problem/D

s1 = input().strip()
s2 = input().strip()

target = sum(1 if ch == "+" else -1 for ch in s1)
current = sum(1 if ch == "+" else -1 for ch in s2 if ch != "?")
unknown = s2.count("?")
ways = 0

for i in range(1 << unknown):
    position = current
    for j in range(unknown):
        position += 1 if (i >> j) & 1 else -1
    if position == target:
        ways += 1

total = 1 << unknown
probability = ways / total
print(f"{probability:.12f}")