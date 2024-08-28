# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        complement = ""
        
        for b in binary:
            complement += '1' if b == '0' else '0'
        return int(complement, 2)