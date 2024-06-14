# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

roads = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            roads += 1

print(roads // 2)