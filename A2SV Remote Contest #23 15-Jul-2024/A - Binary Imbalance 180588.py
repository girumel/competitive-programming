# Problem: A - Binary Imbalance - https://codeforces.com/gym/535309/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    if "0" in s:
        print("YES")
    else:
        print("NO")