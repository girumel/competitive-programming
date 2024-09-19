# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/531416/problem/E

import sys
import threading

def main():
    def dfs(i, j, mark, wall, n, m):
        if mark[i][j] or wall[i][j]:
            return
        mark[i][j] = True
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                dfs(ni, nj, mark, wall, n, m)

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        maze = [input().strip() for _ in range(n)]
        wall = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if maze[i][j] in "#B":
                    wall[i][j] = True
                    if maze[i][j] == "B":
                        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < m:
                                wall[ni][nj] = True
        
        mark = [[False] * m for _ in range(n)]
        dfs(n - 1, m - 1, mark, wall, n, m)

        possible = True
        for i in range(n):
            for j in range(m):
                if maze[i][j] == "G" and not mark[i][j]:
                    possible = False
                    break
            if not possible:
                break

        print("Yes" if possible else "No")

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

thread = threading.Thread(target=main)
thread.start()
thread.join()