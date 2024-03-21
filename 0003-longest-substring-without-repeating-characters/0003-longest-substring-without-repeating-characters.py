class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        longest = 0
    
        start = 0
        for index in range(len(s)):
            if s[index] in unique:
                start = max(unique[s[index]], start)
            
            longest = max(longest, index - start + 1)
            unique[s[index]] = index + 1
            
        return longest