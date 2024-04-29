# Problem: A - FIA Heist - https://codeforces.com/gym/520098/problem/A

string = input()
stack = []

for char in string:
    if char == "<" and stack:
        stack.pop()
    elif char not in ("<", "-"):
        stack.append(char)

print("".join(stack))