# Problem: E - Paul vs Student vs heads - https://codeforces.com/gym/510902/problem/E

n = int(input())
city_a = list(map(int, input().split()))
m = int(input())
city_b = list(map(int, input().split()))

if sum(city_a) != sum(city_b):
    print(-1)
else:
    max_soldiers = 0
    i = j = 0
    sum_a = city_a[0]
    sum_b = city_b[0]

    while i < n and j < m:
        if sum_a == sum_b:
            max_soldiers += 1
            i += 1
            j += 1
            if i < n and j < m:
                sum_a = city_a[i]
                sum_b = city_b[j]
        elif sum_a < sum_b:
            i += 1
            if i < n:
                sum_a += city_a[i]
        else:
            j += 1
            if j < m:
                sum_b += city_b[j]

    print(max_soldiers)