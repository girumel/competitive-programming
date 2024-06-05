# Problem: D - Binary Cut - https://codeforces.com/gym/527307/problem/D

t = int(input())

for _ in range(t):
    s = input()
    count = 1
    target = 0

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            count += 1
        if s[i - 1] == "0" and s[i] == "1":
            target = 1

    print(count - target)