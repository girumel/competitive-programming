class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        target_indices = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                    target_indices.append(i)
        
        return target_indices