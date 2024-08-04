# Problem: Shortest Path to Get All Keys - https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        start, cpt_keys = self.findStartAndKeys(grid, n, m)
        
        queue = deque([(start, '0')])
        visited = set([((0, 0), '0')])
        lvl = 0
        
        while queue:
            for _ in range(len(queue)):
                pos, *keys = queue.popleft()
                r, c = pos

                if len(keys) == cpt_keys + 1:
                    return lvl

                for xr, xc in moves:
                    nr, nc = r + xr, c + xc

                    if not self.isInbound(nr, nc, n, m, grid):
                        continue

                    if not self.canMoveToCell(nr, nc, grid, keys):
                        continue

                    n_keys = self.updateKeys(nr, nc, grid, keys)

                    state = ((nr, nc), *n_keys)
                    if state in visited:
                        continue

                    visited.add(state)
                    queue.append(state)

            lvl += 1

        return -1
    
    def findStartAndKeys(self, grid: List[str], n: int, m: int) -> tuple:
        start = None
        cpt_keys = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].isupper():
                    cpt_keys += 1
        return start, cpt_keys
    
    def isInbound(self, x: int, y: int, n: int, m: int, grid: List[str]) -> bool:
        return 0 <= x < n and 0 <= y < m and grid[x][y] != '#'
    
    def canMoveToCell(self, x: int, y: int, grid: List[str], keys: List[str]) -> bool:
        if grid[x][y].isupper() and not grid[x][y].lower() in keys:
            return False
        return True
    
    def updateKeys(self, x: int, y: int, grid: List[str], keys: List[str]) -> List[str]:
        n_keys = keys.copy()
        if grid[x][y].islower() and grid[x][y] not in keys:
            n_keys.append(grid[x][y])
        return n_keys