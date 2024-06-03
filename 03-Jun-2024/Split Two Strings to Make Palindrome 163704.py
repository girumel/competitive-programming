# Problem: Split Two Strings to Make Palindrome - https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        prefix = 0
        suffix = len(a) - 1

        while prefix < suffix and a[prefix] == b[suffix]:
            prefix += 1
            suffix -= 1

        if is_palindrome(a, prefix, suffix) or is_palindrome(b, prefix, suffix):
            return True
        
        prefix = 0
        suffix = len(a) - 1

        while prefix < suffix and b[prefix] == a[suffix]:
            prefix += 1
            suffix -= 1 

        if is_palindrome(a, prefix, suffix) or is_palindrome(b, prefix, suffix):
            return True
        
        return False