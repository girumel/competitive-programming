# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    print(sum(a[i]), end=' ')
    for j in range(n):
        if a[i][j]:
            print(j+1, end=' ')
    print()