class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = (min(len(word1), len(word2)))
        merged = []
        
        while i < j:
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1

        if len(word1) > i:
            merged.append(word1[i:])
        
        if len(word2) > i:
            merged.append(word2[i:])

        return ''.join(merged)
