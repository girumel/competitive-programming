# Problem: B - Counting Rings - https://codeforces.com/gym/508510/problem/B

shapes = input()
n = len(shapes)

rings = 0 
max_rings = 0

for i in range(n):
    if shapes[i] == 'O':
        rings += 1
        max_rings = max(max_rings, rings)
    else:
        rings = 0
 
print(max_rings)