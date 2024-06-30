# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')

        def is_inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                i, j = r + dr, c + dc
                if is_inbound(i, j) and mat[i][j] > mat[r][c] + 1:
                    mat[i][j] = mat[r][c] + 1
                    queue.append((i, j))

        return mat