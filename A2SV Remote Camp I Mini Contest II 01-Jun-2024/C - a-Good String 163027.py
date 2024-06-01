# Problem: C - a-Good String - https://codeforces.com/gym/522997/problem/C

def count_moves(s, c):
    if len(s) == 1:
        return int(s != c)

    n = len(s)
    m = n // 2
    s1 = s[:m]
    s2 = s[m:]

    count_s1 = m - s1.count(c)
    count_s2 = m - s2.count(c)

    return min(
        count_s1 + count_moves(s2, chr(ord(c) + 1)),
        count_s2 + count_moves(s1, chr(ord(c) + 1)),
    )


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(count_moves(s, "a"))