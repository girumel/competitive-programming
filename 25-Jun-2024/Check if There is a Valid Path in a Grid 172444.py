# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(row, col):
            if not is_valid(row, col) or (row, col) in visited:
                return
            visited.add((row, col))
            for dr, dc in directions[grid[row][col]]:
                r, c = row + dr, col + dc
                if is_valid(r, c) and (-dr, -dc) in directions[grid[r][c]]:
                    dfs(r, c)

        dfs(0, 0)
        
        return (rows-1, cols-1) in visited