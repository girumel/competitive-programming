# Problem: B - Catch Overflow! - https://codeforces.com/gym/520112/problem/B

l = int(input())
stack = [1]
x = 0
max_value = 2**32 - 1
overflown = False

for _ in range(l):
    c = input().strip().split()

    if c[0] == "for":
        n = int(c[1])
        if stack[-1] == -1 or stack[-1] * n > max_value:
            stack.append(-1)
        else:
            stack.append(stack[-1] * n)
    elif c[0] == "add":
        if stack[-1] != -1:
            x += stack[-1]
        else:
            overflown = True
            break
    elif c[0] == "end":
        stack.pop()

    if x > max_value:
        overflown = True
        break

if not overflown:
    print(x)
else:
    print("OVERFLOW!!!")