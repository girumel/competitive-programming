# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
a = list(map(int, input().split()))

min_odd = float("inf")
is_odd = False
total = 0

for num in a:
    if num > 0:
        total += num
    if num % 2 != 0:
        is_odd = True
        min_odd = min(min_odd, abs(num))

if total % 2 == 0:
    total -= min_odd

print(total)