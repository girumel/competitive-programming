# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ (n >> 1)
        return n & (n + 1) == 0

# 101 ^ (101 >> 1) = 101 ^ 010 = 111
# 111 & (111 + 1) = 111 & 1000 = 0

# 1011 ^ (1011 >> 1) = 1011 ^ 0101 = 1110
# 1110 & (1110 + 1) = 1110 & 10000 = 0