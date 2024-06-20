# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(row, col):
            if not is_valid(row, col) or grid[row][col] == '0' or (row, col) in visited:
                return
            visited.add((row, col))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + dr, col + dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)

        return islands