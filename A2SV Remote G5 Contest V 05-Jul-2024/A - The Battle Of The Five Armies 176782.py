# Problem: A - The Battle Of The Five Armies - https://codeforces.com/gym/508510/problem/A

capabilities = list(map(int, input().split()))
soldiers = list(map(int, input().split()))

power_levels = []

for i in range(5):
    power_level = capabilities[i] * soldiers[i]
    power_levels.append(power_level)
    
first_alliance = sum(power_levels[:3])
second_alliance = sum(power_levels[3:])

if first_alliance > second_alliance:
    print("WIN")
elif first_alliance < second_alliance:
    print("LOSE")
else:
    print("DRAW")