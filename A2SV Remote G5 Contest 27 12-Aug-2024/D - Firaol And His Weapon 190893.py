# Problem: D - Firaol And His Weapon - https://codeforces.com/gym/541399/problem/D

n = int(input())
masses = list(map(int, input().split()))

max_mass = max(masses)
freq = [0] * (max_mass + 1)

for mass in masses:
    freq[mass] += 1

dp = [0] * (max_mass + 1)
dp[1] = freq[1]

for i in range(2, max_mass + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + i * freq[i])

print(dp[max_mass])