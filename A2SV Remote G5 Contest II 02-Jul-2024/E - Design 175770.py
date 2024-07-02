# Problem: E - Design - https://codeforces.com/gym/504384/problem/E

from collections import defaultdict

n, q = map(int, input().split())
words = input().split()
word_map = defaultdict(lambda: -1)

for idx, word in enumerate(words):
    for i in range(1, len(word) + 1):
        pref = word[:i]
        for j in range(len(word)):
            suff = word[j:]
            word_map[(pref, suff)] = idx

for _ in range(q):
    pref, suff = input().split()
    print(word_map[(pref, suff)])