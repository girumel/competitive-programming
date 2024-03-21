class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        subs = 0
        prod = 1
        left = 0
        
        if k <= 1:
            return 0
        
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            
            subs += (right-left) + 1

        return subs
                