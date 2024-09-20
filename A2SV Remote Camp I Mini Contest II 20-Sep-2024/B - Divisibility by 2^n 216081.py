# Problem: B - Divisibility by 2^n - https://codeforces.com/gym/522997/problem/B

def count_power(n, p):
    if n == 0:
        return 0
    if n % p != 0:
        return 0
    return 1 + count_power(n // p, p)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    power_count = 0
    power_of_indices = []
    for i in range(n):
        power_count += count_power(a[i], 2)
        power_of_indices.append(count_power(i + 1, 2))

    power_of_indices.sort(reverse=True)
    operations = 0
    while power_count < n and operations < n:
        power_count += power_of_indices[operations]
        operations += 1

    if power_count < n:
        print(-1)
    else:
        print(operations)