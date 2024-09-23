# Problem: B - Shoe Shuffling - https://codeforces.com/gym/518838/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    sizes = list(map(int, input().split())) + [float("inf")]

    # freq = {}
    # for size in sizes:
    #     if size in freq:
    #         freq[size] += 1
    #     else:
    #         freq[size] = 1

    # if any(count == 1 for count in freq.values()):
    #     print(-1)
    #     break

    perms = []
    index = 0
    group = 1
    valid = True

    for i in range(1, n + 1):
        if sizes[i] == sizes[i - 1]:
            group += 1
        else:
            if group == 1:
                valid = False
                break
            perms.append(i)
            perms.extend(range(index + 1, i))
            index = i
            group = 1

    print(*perms) if valid else print("-1")