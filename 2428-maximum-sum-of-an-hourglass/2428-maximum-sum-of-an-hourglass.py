class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                hourglass = grid[r-1][c-1:c+2] + [grid[r][c]] + grid[r+1][c-1:c+2]
                max_sum = max(max_sum, sum(hourglass))

        return max_sum
    