# Problem: B - Drinks - https://codeforces.com/gym/500425/problem/B

n = int(input())
p = list(map(int, input().split()))
print(((sum(p)/100) / n) * 100)