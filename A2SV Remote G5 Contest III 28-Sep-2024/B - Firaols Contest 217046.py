# Problem: B - Firaols Contest - https://codeforces.com/gym/505936/problem/B

n, m = map(int, input().split())
difficulties = list(map(int, input().split()))

counts = [0] * (n + 1)
unique = set()
result = []

for difficulty in difficulties:
    counts[difficulty] += 1
    unique.add(difficulty)

    if len(unique) == n:
        result.append(1)
        for i in range(1, n + 1):
            counts[i] -= 1
            if counts[i] == 0:
                unique.remove(i)
    else:
        result.append(0)

print("".join(map(str, result)))