# Problem: D - Truth and Illusion - https://codeforces.com/gym/505936/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]

    operations = 0
    
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            cells = [
                (i, j),
                (n - 1 - j, i),
                (n - 1 - i, n - 1 - j),
                (j, n - 1 - i),
            ]
            ones = sum(grid[x][y] for x, y in cells)
            zeros = 4 - ones
            operations += min(ones, zeros)
    
    print(operations)