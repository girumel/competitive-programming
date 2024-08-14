# Problem: Topological Sort - https://codeforces.com/problemset/gymProblem/101102/K

from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    to_remove = defaultdict(set)

    for _ in range(m):
        a, b = map(int, input().split())
        to_remove[b].add(a)

    ans = list(range(1, n + 1))

    for i in range(1, n + 1):
        left = i - 2
        while left >= 0 and ans[left] in to_remove[i]:
            ans[left], ans[left + 1] = ans[left + 1], ans[left]
            left -= 1

    print(*ans)