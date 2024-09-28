# Problem: D - Lanterns - https://codeforces.com/gym/507024/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    lanterns = [tuple(map(int, input().split())) for _ in range(n)]

    lanterns.sort(key=lambda x: (x[0], -x[1]))

    index, count, total = 0, 0, 0
    for i in range(len(lanterns)):
        if i < index:
            continue
        total += lanterns[i][1]
        count += 1
        while index < len(lanterns) and lanterns[index][0] <= count:
            index += 1
        count = max(0, i - index + 1)

    print(total)