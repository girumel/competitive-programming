# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))

i, j, total, max_books = 0, 0, 0, 0

while j < n:
    total += a[j]
    while total > t:
        total -= a[i]
        i += 1
    max_books = max(max_books, j - i + 1)
    j += 1

print(max_books)