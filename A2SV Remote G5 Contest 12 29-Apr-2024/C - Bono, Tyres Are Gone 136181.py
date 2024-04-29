# Problem: C - Bono, Tyres Are Gone - https://codeforces.com/gym/520098/problem/C

n = int(input())
tire_stack = []
reordering = 0
required_tire = 1

for _ in range(2*n):
    cmd, *args = input().split()
    if cmd == "add":
        tire_stack.append(int(args[0]))
    else:
        if tire_stack and tire_stack[-1] != required_tire:
            reordering += 1
            tire_stack.clear()
        elif tire_stack:
            tire_stack.pop()
        required_tire += 1

print(reordering)