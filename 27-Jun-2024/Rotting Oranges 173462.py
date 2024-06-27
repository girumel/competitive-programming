# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh_oranges = 0
        queue = deque()
        minutes = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        def is_inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        while queue:
            row, col, time = queue.popleft()
            minutes = time
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if is_inbound(r, c) and grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh_oranges -= 1
                    queue.append((r, c, time + 1))

        return minutes if fresh_oranges == 0 else -1
