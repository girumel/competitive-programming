# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0] * n
        left_diagonal = [0] * (2 * n - 1)
        right_diagonal = [0] * (2 * n - 1)
        queens = set()
        solutions = []

        def is_safe(row, col):
            return not (cols[col] + left_diagonal[row - col] + right_diagonal[row + col])

        def backtrack(row):
            for col in range(n):
                if is_safe(row, col):
                    # place queen
                    queens.add((row, col))
                    cols[col] = 1
                    left_diagonal[row - col] = 1
                    right_diagonal[row + col] = 1
                    
                    # add solution
                    if row + 1 == n:
                        solution = []
                        for _, col in sorted(queens):
                            solution.append('.' * col + 'Q' + '.' * (n - col - 1))
                        solutions.append(solution)
                    else:
                        backtrack(row + 1)

                    # remove queen
                    queens.remove((row, col))
                    cols[col] = 0
                    left_diagonal[row - col] = 0
                    right_diagonal[row + col] = 0

        backtrack(0)

        return solutions