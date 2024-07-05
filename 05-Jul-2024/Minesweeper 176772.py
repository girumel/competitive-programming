# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        def is_inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        def dfs(row, col):
            if not is_inbound(row, col):
                return
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            if board[row][col] != 'E':
                return
            
            mines = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if is_inbound(nr, nc) and board[nr][nc] == 'M':
                    mines += 1
            
            if mines > 0:
                board[row][col] = str(mines)
                return
            
            board[row][col] = 'B'
            for dr, dc in directions:
                dfs(row + dr, col + dc)
                
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)
        
        return board