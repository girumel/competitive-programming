# Problem: B - Operation 1 - https://codeforces.com/gym/521860/problem/B

a, m = map(int, input().split())

ops = (a + 1) // 2
max_ops = ops - a % 2

while ops % m != 0 and ops - (a + 1) // 2 < max_ops:
    ops += 1

print(ops if ops % m == 0 else -1)