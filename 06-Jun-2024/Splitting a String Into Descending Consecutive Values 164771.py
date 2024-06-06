# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start, previous):
            # Base case: if we reach the end of the string
            if start == len(s):
                return True
            
            # Recursive relation: check all possible substrings starting from start
            for index in range(start, len(s)):
                current = int(s[start:index+1])
                if current == previous - 1: 
                    if backtrack(index+1, current):
                        return True
                elif current >= previous: 
                    break
            return False
        
        # Check all possible initial substrings
        for i in range(1, len(s)):
            initial = int(s[:i])
            if backtrack(i, initial):
                return True
        
        return False