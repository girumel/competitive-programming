# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        visited = set()
        queue = deque([(1, 0)])

        def get_pos(pos, n):
            row = n - 1 - (pos - 1) // n
            col = (pos - 1) % n
            if row % 2 == n % 2:
                return row, n - 1 - col
            return row, col
        
        while queue:
            current, steps = queue.popleft()
            if current == target:
                return steps
            if current in visited:
                continue
            visited.add(current)
            for i in range(1, 7):
                next_pos = current + i
                if next_pos > target:
                    break
                row, col = get_pos(next_pos, n)
                if board[row][col] != -1:
                    next_pos = board[row][col]
                queue.append((next_pos, steps + 1))
        return -1