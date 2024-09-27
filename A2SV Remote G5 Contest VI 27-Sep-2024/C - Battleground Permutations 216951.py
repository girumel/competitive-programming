# Problem: C - Battleground Permutations - https://codeforces.com/gym/510902/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    cheifu = list(map(int, input().split()))
    opponent = list(map(int, input().split()))

    cheifu.sort(reverse=True)
    opponent.sort(reverse=True)

    arrangements = 1
    MOD = 10**9 + 7
    
    j = 0
    for i in range(n):
        while j < n and cheifu[j] > opponent[i]:
            j += 1
        arrangements *= j - i
        arrangements %= MOD
        if arrangements == 0:
            break

    print(arrangements)