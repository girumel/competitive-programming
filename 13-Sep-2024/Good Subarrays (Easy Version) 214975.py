# Problem: Good Subarrays (Easy Version) - https://codeforces.com/problemset/problem/1736/C1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 1
    pairs = 0
    for num in a:
        if num >= count:
            count += 1
        else:
            if count > 1:
                pairs += count * (count - 1) // 2
                pairs -= num * (num - 1) // 2
            count = num + 1
    
    if count > 1:
        pairs += count * (count - 1) // 2

    print(pairs)