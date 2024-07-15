# Problem: C - The Lakes - https://codeforces.com/gym/535309/problem/C

from collections import deque

def is_inbound(rows, cols, row, col, grid, visited):
    return (
        0 <= row < rows
        and 0 <= col < cols
        and grid[row][col] > 0
        and not visited[row][col]
    )

def bfs(rows, cols, sr, sc, grid, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(sr, sc)])
    visited[sr][sc] = True
    depth = grid[sr][sc]

    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if is_inbound(rows, cols, nr, nc, grid, visited):
                visited[nr][nc] = True
                depth += grid[nr][nc]
                queue.append((nr, nc))

    return depth

t = int(input())
for _ in range(t):
    rows, cols = map(int, input().split())
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))

    visited = [[False] * cols for _ in range(rows)]
    largest = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0 and not visited[row][col]:
                volume = bfs(rows, cols, row, col, grid, visited)
                largest = max(largest, volume)

    print(largest)