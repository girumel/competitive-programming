# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        singles = []
        
        for num in nums:
            if num in singles:
                singles.remove(num)
            else:
                singles.append(num)
                
        return singles