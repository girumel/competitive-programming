class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        if n < 5:
            return 0

        vowels = "aeiou"
        counts = [0] * 5

        longest = left = 0
        for right in range(n):
            if word[right] in vowels:
                if right > 0 and vowels.index(word[right]) < vowels.index(word[right - 1]):
                    counts = [0] * 5
                    left = right
                counts[vowels.index(word[right])] += 1
                
                if all(counts):
                    longest = max(longest, right - left + 1)
        
        return longest