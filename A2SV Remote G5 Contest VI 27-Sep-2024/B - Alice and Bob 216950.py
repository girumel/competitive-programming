# Problem: B - Alice and Bob - https://codeforces.com/gym/510902/problem/B

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    alice = sorted(input())
    bob = sorted(input())
    index_a, index_b = 0, 0
    count_a, count_b = 0, 0
    smallest = []

    while index_a < n and index_b < m:
        if (alice[index_a] < bob[index_b] and count_a < k) or count_b == k:
            smallest.append(alice[index_a])
            count_a += 1
            count_b = 0
            index_a += 1
        else:
            smallest.append(bob[index_b])
            count_b += 1
            count_a = 0
            index_b += 1

    print("".join(smallest))