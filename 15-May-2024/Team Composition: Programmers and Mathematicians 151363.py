# Problem: Team Composition: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    min_students = min(a, b)
    max_teams = (a + b) // 4
    print(min(min_students, max_teams))