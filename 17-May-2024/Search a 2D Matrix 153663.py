# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            cell = matrix[mid // cols][mid % cols]

            if cell == target:
                return True
            elif cell < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False