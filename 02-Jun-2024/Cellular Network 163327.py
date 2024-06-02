# Problem: Cellular Network - https://codeforces.com/contest/702/problem/C

num_cities, num_towers = map(int, input().split())
cities = sorted(map(int, input().split()))
towers = sorted(map(int, input().split()))

max_dist = 0
city_ptr = tower_ptr = 0

for city_ptr in range(num_cities):
    while tower_ptr < num_towers - 1:
        next_dist = abs(cities[city_ptr] - towers[tower_ptr + 1])
        curr_dist = abs(cities[city_ptr] - towers[tower_ptr])
        if next_dist <= curr_dist:
            tower_ptr += 1
        else:
            break
    max_dist = max(max_dist, abs(cities[city_ptr] - towers[tower_ptr]))

print(max_dist)