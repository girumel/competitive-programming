# Problem: D - Minimum Park Lighting Cost - https://codeforces.com/gym/537575/problem/D

from itertools import combinations

def is_valid(parks, lights, combination):
    light_levels = [0] * 101

    for light_index in combination:
        a, b, p, _ = lights[light_index]
        for pos in range(a, b + 1):
            light_levels[pos] += p

    for s, t, c in parks:
        for pos in range(s, t + 1):
            if light_levels[pos] < c:
                return False
    return True

n, m = map(int, input().split())
parks = []
lights = []

for _ in range(n):
    s, t, c = map(int, input().split())
    parks.append((s, t, c))

for _ in range(m):
    a, b, p, _ = map(int, input().split())
    lights.append((a, b, p, _))

min_cost = float("inf")
for r in range(1, m + 1):
    for combination in combinations(range(m), r):
        if is_valid(parks, lights, combination):
            cost = sum(lights[i][3] for i in combination)
            min_cost = min(min_cost, cost)

print(min_cost)