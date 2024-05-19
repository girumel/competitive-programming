# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(s):
            return s[::-1]

        def invert(s): # invert all the bits in s
            return ''.join(['1' if c == '0' else '0' for c in s])
        
        s = "0"
        for i in range(2, n+1):
            s = s + "1" + reverse(invert(s))
            if len(s) >= k:
                return s[k-1]
        return s[k-1]