# Problem: D - Conveyor Belts - https://codeforces.com/gym/500425/problem/D

t = int(input())

for _ in range(t):
    n, x1, y1, x2, y2 = map(int, input().split())

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    x1 = min(x1, n - x1 - 1)
    y1 = min(y1, n - y1 - 1)
    x2 = min(x2, n - x2 - 1)
    y2 = min(y2, n - y2 - 1)

    min_energy = abs(min(x1, y1) - min(x2, y2))
    
    print(min_energy)