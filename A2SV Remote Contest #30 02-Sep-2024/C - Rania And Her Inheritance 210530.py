# Problem: C - Rania And Her Inheritance - https://codeforces.com/gym/545837/problem/C

from itertools import combinations

n, m = map(int, input().split())
experts = []
rivalries = []

for _ in range(n):
    experts.append(input().strip())
for _ in range(m):
    rivalries.append(tuple(input().strip().split()))

riv_dict = {expert: set() for expert in experts}
for a, b in rivalries:
    riv_dict[a].add(b)
    riv_dict[b].add(a)

def is_valid_team(team):
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            if team[j] in riv_dict[team[i]]:
                return False
    return True

for size in range(n, 0, -1):
    for team in combinations(experts, size):
        if is_valid_team(team):
            print(size)
            for member in sorted(team):
                print(member)
            exit()