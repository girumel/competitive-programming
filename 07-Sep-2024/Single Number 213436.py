# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        
        for num in nums:
            single ^= num
            
        return single