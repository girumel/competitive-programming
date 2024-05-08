# Problem: A - Problemsolving Log - https://codeforces.com/gym/522997/problem/A

from collections import defaultdict

t = int(input())

difficulty = {chr(i): i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}

for _ in range(t):
    n = int(input())
    log = input()
    count = defaultdict(int)
    solved = 0

    for problem in log:
        count[problem] += 1

    for problem, time_spent in count.items():
        if difficulty[problem] <= time_spent:
            solved += 1

    print(solved)