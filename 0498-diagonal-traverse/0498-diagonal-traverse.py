class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # upward (even rows and cols)
        # r-1, c+1 until r >= 0 and c < cols

        # downward (odd rows and cols)
        # r+1, c-1 until r < rows and c >= 0

        rows = len(mat)
        cols = len(mat[0])
        diagonals = []

        for i in range(rows + cols - 1):
            if i % 2 == 0:
                r = min(i, rows - 1)
                c = max(0, i - rows + 1)
                while r >= 0 and c < cols:
                    diagonals.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                r = max(0, i - cols + 1)
                c = min(i, cols - 1)
                while r < rows and c >= 0:
                    diagonals.append(mat[r][c])
                    r += 1
                    c -= 1
        
        return diagonals