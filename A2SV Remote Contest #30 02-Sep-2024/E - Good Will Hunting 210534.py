# Problem: E - Good Will Hunting - https://codeforces.com/gym/545837/problem/E

l, r = map(int, input().split())

max_xor = 1
diff = l ^ r

while diff > 0:
    max_xor <<= 1
    max_xor |= 1
    diff >>= 1

print(max_xor >> 1)