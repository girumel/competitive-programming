# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def is_inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        
        while queue:
            row, col, steps = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if is_inbound(nr, nc) and maze[nr][nc] == '.':
                    if nr in (0, n - 1) or nc in (0, m - 1):
                        return steps + 1
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
                                 
        return -1