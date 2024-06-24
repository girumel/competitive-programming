# Problem: A - Flag - https://codeforces.com/gym/531416/problem/A

n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

for i in range(n):
    for j in range(m - 1):
        if flag[i][j] != flag[i][j + 1]:
            print("NO")
            exit()
# else:
#     print("YES")

for i in range(m):
    for j in range(n - 1):
        if flag[j][i] == flag[j + 1][i]:
            print("NO")
            exit()
print("YES")