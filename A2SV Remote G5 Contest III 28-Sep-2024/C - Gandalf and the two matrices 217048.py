# Problem: C - Gandalf and the two matrices - https://codeforces.com/gym/505936/problem/C

n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [[0] * m for _ in range(n)]

operations = []
updates = set()

for i in range(n - 1):
    for j in range(m - 1):
        if all(
            matrix_a[x][y] == 1
            for x, y in [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
        ):
            operations.append((i + 1, j + 1))
            for x, y in [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]:
                matrix_b[x][y] = 1
                updates.add((x, y))

if any(
    (i, j) not in updates and matrix_a[i][j] != matrix_b[i][j]
    for i in range(n)
    for j in range(m)
):
    print(-1)
else:
    print(len(operations))
    for x, y in operations:
        print(x, y)