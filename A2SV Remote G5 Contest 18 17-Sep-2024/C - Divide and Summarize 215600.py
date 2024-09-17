# Problem: C - Divide and Summarize - https://codeforces.com/gym/528793/problem/C

def divide(min_a, max_a, a, possible_sums):
    total = sum(a[min_a : max_a + 1])
    possible_sums.add(total)
    mid = (a[min_a] + a[max_a]) // 2
    pos = -1
    for i in range(min_a, max_a + 1):
        if a[i] <= mid:
            pos = i
        else:
            break
    if pos == -1 or pos == max_a:
        return
    divide(min_a, pos, a, possible_sums)
    divide(pos + 1, max_a, a, possible_sums)

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    possible_sums = set()
    divide(0, n - 1, a, possible_sums)
    for _ in range(q):
        s = int(input())
        if s in possible_sums:
            print("Yes")
        else:
            print("No")