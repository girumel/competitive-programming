class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        alphanums = []
        alphanums.extend(range(48, 58))
        alphanums.extend(range(65, 91))
        alphanums.extend(range(97, 123))
        
        while l < r:
            while l < r and ord(s[l]) not in alphanums:
                l += 1
            while r > l and ord(s[r]) not in alphanums:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
