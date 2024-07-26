# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = {} # char: count
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        most_freq = max(freq.values())
        
        if most_freq > (n+1) // 2:
            return ""
        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        ans = [None] * n
        i = 0
        for char, count in sorted_freq:
            for j in range(count):
                ans[i] = char
                i += 2
                if i >= n:
                    i = 1
        
        return "".join(ans)