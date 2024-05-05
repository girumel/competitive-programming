# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        start, brackets, repeats = 0, 0, 0
        result = ""

        for i, ch in enumerate(s):
            if brackets == 0 and ch.islower():
                result += ch
                start = i + 1
            if ch == "[":
                brackets += 1
                if brackets == 1:
                    repeats = int(s[start:i])
                    start = i + 1
            elif ch == "]":
                brackets -= 1
                if brackets == 0:
                    result += self.decodeString(s[start:i]) * repeats
                    start = i + 1
        
        return result