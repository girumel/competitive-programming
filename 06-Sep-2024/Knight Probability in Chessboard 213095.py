# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0]*n for _ in range(n)]
        dp[row][column] = 1
        
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                      (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        for _ in range(k):
            new_dp = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            new_dp[x][y] += dp[i][j]
            dp = new_dp
        return sum(sum(row) for row in dp) / 8**k