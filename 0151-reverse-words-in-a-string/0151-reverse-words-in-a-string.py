class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(reversed([w for w in s.split()])))