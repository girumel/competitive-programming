class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        shifted = []

        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
        for i in range(n):
            shifted.append(chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a')))
        
        return ''.join(shifted)