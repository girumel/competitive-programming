# Problem: E - Minimum Ties - https://codeforces.com/gym/521860/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    results = []
    win = (n - 1) // 2
    results.extend([1] * win)
    if n % 2 == 0:
        results.append(0)
    results.extend([-1] * win)
    
    for i in range(1, n + 1):
        for j in range(n - i):
            print(results[j], end=" ")
    print()