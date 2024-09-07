# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        twice = 0
        
        for num in nums:
            twice |= single & num
            single ^= num
            common = single & twice
            single &= ~common
            twice &= ~common
        
        return single