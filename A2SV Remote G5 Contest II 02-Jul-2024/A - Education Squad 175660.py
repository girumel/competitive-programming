# Problem: A - Education Squad - https://codeforces.com/gym/504384/problem/A

grid = [input(), input(), input()]

individual_winners = set()
team_winners = set()

def add_winner(line):
    unique_heads = set(line)
    if len(unique_heads) == 1:
        individual_winners.add(line[0])
    elif len(unique_heads) == 2:
        team_winners.add("".join(sorted(unique_heads)))


for i in range(3):
    add_winner(grid[i])
    add_winner(grid[0][i] + grid[1][i] + grid[2][i])

add_winner(grid[0][0] + grid[1][1] + grid[2][2])
add_winner(grid[0][2] + grid[1][1] + grid[2][0])

print(len(individual_winners))
print(len(team_winners))