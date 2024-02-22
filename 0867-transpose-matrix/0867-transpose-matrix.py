class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(matrix[0])):
            transposed.append([row[i] for row in matrix])
            
        return transposed