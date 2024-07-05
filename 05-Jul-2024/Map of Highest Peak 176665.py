# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        heights = [[-1] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        for i, row in enumerate(isWater):
            for j, val in enumerate(row):
                if val:
                    queue.append((i, j))
                    heights[i][j] = 0
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_inbound(nx, ny) and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    queue.append((nx, ny))
        
        return heights