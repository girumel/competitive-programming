# Problem: B - Amro and Bits - https://codeforces.com/gym/545837/problem/B

t = int(input())
for _ in range(t):
    number = int(input())

    if number == 1:
        print(3)
        continue

    zero_pos = None
    one_pos = None
    ones = 0

    for pos, bit in enumerate(bin(number)[2:][::-1]):
        if bit == "0" and zero_pos is None:
            zero_pos = pos
        elif bit == "1":
            if one_pos is None:
                one_pos = pos
            ones += 1

    if ones > 1:
        print(2**one_pos)
    else:
        print(2**zero_pos + 2**one_pos)