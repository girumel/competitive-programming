# Problem: C - Smeagol's Riddle - https://codeforces.com/gym/508510/problem/C

n = int(input())
for _ in range(n):
    word = input()
    count = 0
    
    for i in range(len(word) // 2):
        if word[i] != word[-i-1]:
            count += 1
    
    print(count)