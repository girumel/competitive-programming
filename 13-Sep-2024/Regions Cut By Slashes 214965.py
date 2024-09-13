# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(n * n * 4)]
        
        def index(i, j, k):
            return (i * n + j) * 4 + k
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
            
        for i in range(n):
            for j in range(n):
                if i > 0:
                    union(index(i, j, 0), index(i - 1, j, 2))
                if j > 0:
                    union(index(i, j, 3), index(i, j - 1, 1))
                if grid[i][j] != '/':
                    union(index(i, j, 0), index(i, j, 1))
                    union(index(i, j, 2), index(i, j, 3))
                if grid[i][j] != '\\':
                    union(index(i, j, 0), index(i, j, 3))
                    union(index(i, j, 1), index(i, j, 2))
                    
        return len(set(find(x) for x in range(n * n * 4)))