class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        if n < 5:
            return 0

        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_index = {v: i for i, v in enumerate(vowels)}
        counts = [0]*5

        longest = left = 0
        for right in range(n):
            if word[right] in vowel_index:
                if right > 0 and vowel_index[word[right]] < vowel_index[word[right - 1]]:
                    counts = [0]*5
                    left = right
                counts[vowel_index[word[right]]] += 1
                
                if all(counts):
                    longest = max(longest, right - left + 1)
        
        return longest