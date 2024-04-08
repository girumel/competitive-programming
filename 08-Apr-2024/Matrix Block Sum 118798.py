# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        ps = [[0] * (cols+1) for _ in range(rows+1)]
        ans = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                ps[i+1][j+1] = mat[i][j] + ps[i+1][j] + ps[i][j+1] - ps[i][j]
        
        for i in range(rows):
            for j in range(cols):
                max_row = max(0, i-k)
                max_col = max(0, j-k)
                min_row = min(rows, i+k+1)
                min_col = min(cols, j+k+1)
                ans[i][j] = ps[min_row][min_col] - ps[max_row][min_col] - ps[min_row][max_col] + ps[max_row][max_col]
                
        return ans
    