# Problem: E - Allison's Game - https://codeforces.com/gym/520098/problem/E

n = int(input())
heights = list(map(int, input().split()))
heights.append(0)
stack = []
max_length = 0

for i in range(len(heights)):
    while stack and heights[stack[-1]] >= heights[i]:
        h = heights[stack.pop()]
        if not stack:
            width = i
        else:
            width = i - stack[-1] - 1
        length = min(h, width)
        max_length = max(max_length, length)
    stack.append(i)

print(max_length)