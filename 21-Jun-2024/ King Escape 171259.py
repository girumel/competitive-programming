# Problem:  King Escape - https://codeforces.com/problemset/problem/1033/A

n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

top_left = ax < bx and ay < by and ax < cx and ay < cy
top_right = ax > bx and ay < by and ax > cx and ay < cy
bottom_right = ax > bx and ay > by and ax > cx and ay > cy
bottom_left = ax < bx and ay > by and ax < cx and ay > cy

if top_left or top_right or bottom_right or bottom_left:
    print("YES")
else:
    print("NO")