# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Base cases: empty string, all lowercase, all uppercase
        if len(s) < 2 or s.islower() or s.isupper():
            return ""
        
        # Recursive relation: if a character is not in both cases, split the string at that character
        for i in range(len(s)):
            if s[i].lower() not in s or s[i].upper() not in s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        
        return s