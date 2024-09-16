# Problem: A - Largest Subsequence - https://codeforces.com/gym/520112/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())

    stack = []
    for i in range(n):
        while stack and s[i] > s[stack[-1]]:
            stack.pop()
        stack.append(i)

    size = len(stack)
    first_char = s[stack[0]]
    dup_count = sum(1 for i in stack if s[i] == first_char)

    for i in range(size // 2):
        s[stack[i]], s[stack[size - 1 - i]] = s[stack[size - 1 - i]], s[stack[i]]

    if list(s) == sorted(s):
        print(size - dup_count)
    else:
        print(-1)