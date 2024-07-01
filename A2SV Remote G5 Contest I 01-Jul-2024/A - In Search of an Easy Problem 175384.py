# Problem: A - In Search of an Easy Problem - https://codeforces.com/gym/500425/problem/A

n = int(input())
o = list(map(int, input().split()))
if 1 in o:
    print("HARD")
else:
    print("EASY")