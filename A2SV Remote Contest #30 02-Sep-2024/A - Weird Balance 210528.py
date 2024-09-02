# Problem: A - Weird Balance - https://codeforces.com/gym/545837/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    ages = list(map(int, input().split()))

    ages.sort(reverse=True)
    max_age = ages[0]

    i = 1
    while i < n and ages[i] == max_age:
        i += 1

    if i == n:
        print("NO")
    else:
        ages[0], ages[i] = ages[i], max_age
        print("YES")
        print(*ages)