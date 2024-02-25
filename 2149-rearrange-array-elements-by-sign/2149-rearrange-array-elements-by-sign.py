class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearranged = [0]*len(nums)
        pos_nums = [n for n in nums if n > 0]
        neg_nums = [n for n in nums if n < 0]
        
        for i in range(len(nums) // 2):
            rearranged[2*i] = pos_nums[i]
            rearranged[2*i+1] = neg_nums[i]
        
        return rearranged
                