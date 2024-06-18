# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0] * n
        left_diagonal = [0] * (2 * n - 1)
        right_diagonal = [0] * (2 * n - 1)
        queens = set()
        solutions = []

        def is_safe(row, col):
            return not (cols[col] + left_diagonal[row - col] + right_diagonal[row + col])
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            left_diagonal[row - col] = 1
            right_diagonal[row + col] = 1
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            left_diagonal[row - col] = 0
            right_diagonal[row + col] = 0
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            solutions.append(solution)

        def backtrack(row):
            for col in range(n):
                if is_safe(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        backtrack(0)

        return solutions