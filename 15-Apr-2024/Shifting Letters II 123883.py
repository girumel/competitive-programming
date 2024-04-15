# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shifts = [0] * len(s)
        final_string = ""

        for start, end, direction in shifts:
            total_shifts[start] += (1 if direction else -1)
            if end + 1 < len(s):
                total_shifts[end + 1] -= (1 if direction else -1)

        for i in range(1, len(s)):
            total_shifts[i] += total_shifts[i - 1]

        for i in range(len(s)):
            shift = total_shifts[i] % 26
            final_string += chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))

        return final_string