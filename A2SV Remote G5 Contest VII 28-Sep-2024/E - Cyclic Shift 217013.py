# Problem: E - Cyclic Shift - https://codeforces.com/gym/511771/problem/E

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

min_moves = float("inf")
shift_cost = [[0] * m for _ in range(n)]

for i in range(n):
    if "0" * m == matrix[i]:
        print(-1)
        exit()

    row = matrix[i]
    extended_row = row * 3
    row_len = len(row)
    left = right = row_len

    while extended_row[left] != "1":
        left -= 1

    for j in range(row_len, 2 * row_len):
        while right < j or extended_row[right] != "1":
            right += 1

        if extended_row[j] == "1":
            left = j

        shift_cost[i][j - row_len] = min(right - j, j - left)

for col in range(m):
    total_cost = sum(shift_cost[row][col] for row in range(n))
    min_moves = min(min_moves, total_cost)

print(min_moves)