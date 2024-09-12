# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

n = int(input())
s = input()

pokemons = set(s)
count = {}
min_flats = n
left = right = current = 0

while left <= right:
    if current == len(pokemons):
        min_flats = min(min_flats, right - left)
        count[s[left]] -= 1
        if count[s[left]] == 0:
            current -= 1
        left += 1
    elif right < n:
        if s[right] not in count or count[s[right]] == 0:
            current += 1
        count[s[right]] = count.get(s[right], 0) + 1
        right += 1
    else:
        break

print(min_flats)