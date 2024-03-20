class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}
        window = {}
        anagram_indices = []
        k = len(p)
        
        for c in p:
            if c in target:
                target[c] += 1
            else:
                target[c] = 1
        
    
        for i in range(len(s)):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
            
            if i >= k:
                leftmost = i - k
                if window[s[leftmost]] == 1:
                    del window[s[leftmost]]
                else:
                    window[s[leftmost]] -= 1
            
            
            if window == target:
                anagram_indices.append(i - k + 1)
        
        return anagram_indices
            
        