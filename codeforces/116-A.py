n = int(input())
capacity = 0
tram = 0
for _ in range(n):
    exit, enter = map(int, input().split())
    tram -= exit
    tram += enter
    capacity = max(tram, capacity)
print(capacity)
