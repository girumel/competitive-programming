# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        
        while queue:
            i, j, d = queue.popleft()
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    grid[ni][nj] = d + 1
                    queue.append((ni, nj, d + 1))
        
        return d