# Problem: Construct Product Matrix - https://leetcode.com/problems/construct-product-matrix/description/

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        product = [[1] * m for _ in range(n)]

        forward = 1
        for i in range(n):
            for j in range(m):
                product[i][j] = forward % 12345
                forward = (forward * grid[i][j]) % 12345

        backward = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product[i][j] = (product[i][j] * backward) % 12345
                backward = (backward * grid[i][j]) % 12345

        return product