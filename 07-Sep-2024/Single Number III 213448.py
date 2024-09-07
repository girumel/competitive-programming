# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        singles = 0
        for num in nums:
            singles ^= num
            
        diff = singles & -singles
        single1 = 0
        single2 = 0
        for num in nums:
            if num & diff:
                single1 ^= num
            else:
                single2 ^= num
                
        return [single1, single2]