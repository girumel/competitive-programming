# Problem: C - Poisoned Dagger - https://codeforces.com/gym/523225/problem/C

def is_possible(a, duration, h):
    damage = 0
    for i in range(len(a) - 1):
        damage += min(a[i + 1] - a[i], duration)
    return (damage + duration) >= h

t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    low, high = 0, 10**18
    min_k = 0
    while low <= high:
        mid = (low + high) // 2
        if is_possible(a, mid, h):
            min_k = mid
            high = mid - 1
        else:
            low = mid + 1

    print(min_k)