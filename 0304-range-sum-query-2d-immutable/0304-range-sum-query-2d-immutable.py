class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        matrix.append([0] * cols)
        for r in range(rows):
            matrix[r].append(0)

        for r in range(rows):
            for c in range(cols):
                top = matrix[r-1][c]
                left = matrix[r][c-1]
                top_left = matrix[r-1][c-1]
                matrix[r][c] += top + left - top_left

        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.matrix[row1-1][col2]
        left = self.matrix[row2][col1-1]
        top_left = self.matrix[row1-1][col1-1]

        return self.matrix[row2][col2] - top - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)