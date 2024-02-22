class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majorities = set()
        for num in nums:
            if nums.count(num) > len(nums)/3:
                majorities.add(num)
        
        return list(majorities)