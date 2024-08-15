# Problem: E - Barcode - https://codeforces.com/gym/541399/problem/E

n, m, x, y = map(int, input().split())
picture = [input() for _ in range(n)]
dp = [[float("inf")] * 2 for _ in range(m + 1)]
dp[0] = [0, 0]

whites = [0] * (m + 1)
blacks = [0] * (m + 1)

for j in range(1, m + 1):
    whites[j] = whites[j - 1] + sum(1 for i in range(n) if picture[i][j - 1] == ".")
    blacks[j] = blacks[j - 1] + sum(1 for i in range(n) if picture[i][j - 1] == "#")

for i in range(1, m + 1):
    for j in range(x, y + 1):
        if j > i:
            continue
        dp[i][0] = min(dp[i][0], dp[i - j][1] + whites[i] - whites[i - j])
        dp[i][1] = min(dp[i][1], dp[i - j][0] + blacks[i] - blacks[i - j])

print(min(dp[m][0], dp[m][1]))