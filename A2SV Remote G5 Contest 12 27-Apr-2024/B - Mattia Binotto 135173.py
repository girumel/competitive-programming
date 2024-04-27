# Problem: B - Mattia Binotto - https://codeforces.com/gym/520098/problem/B

n = int(input())
t = list(map(int, input().split()))
t.sort()
wait = 0
count = 0

for i in range(n):
    if wait <= t[i]:
        count += 1
        wait += t[i]

print(count)