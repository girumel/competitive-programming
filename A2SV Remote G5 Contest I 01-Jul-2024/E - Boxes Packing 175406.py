# Problem: E - Boxes Packing - https://codeforces.com/gym/500425/problem/E

from collections import Counter

n = int(input())
boxes = list(map(int, input().split()))
count = Counter(boxes)

print(max(count.values()))