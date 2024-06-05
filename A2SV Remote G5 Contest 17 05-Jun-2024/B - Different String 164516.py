# Problem: B - Different String - https://codeforces.com/gym/527307/problem/B

t = int(input())

for _ in range(t):
    s = input()
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            s = s[: i - 1] + s[i] + s[i - 1] + s[i + 1 :]
            print("YES")
            print(s)
            break
    else:
        print("NO")