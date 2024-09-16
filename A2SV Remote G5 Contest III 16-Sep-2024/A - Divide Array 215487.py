# Problem: A - Divide Array - https://codeforces.com/gym/505936/problem/A

n = int(input())
nums = list(map(int, input().split()))

positive = []
negative = []
zero = []

for num in nums:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

if len(negative) > 1:
    if not positive:
        positive.extend(negative[1:3])
        zero.extend(negative[3:])
    else:
        zero.extend(negative[1:])
    negative = negative[:1]

print(len(negative), *negative)
print(len(positive), *positive)
print(len(zero), *zero)