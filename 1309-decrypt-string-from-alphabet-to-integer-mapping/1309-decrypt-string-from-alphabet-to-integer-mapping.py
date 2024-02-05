class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapped = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                mapped += chr(ord("a") + int(s[i:i+2]) - 1)
                i += 3
            else:
                mapped += chr(ord("a") + int(s[i]) - 1)
                i += 1
        return mapped
