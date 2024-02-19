class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_to_index = {num: i for i, num in enumerate(nums)}
        
        for operation in operations:
            old_num, new_num = operation
            index = num_to_index[old_num]
            nums[index] = new_num
            num_to_index[new_num] = index
            del num_to_index[old_num]

        return nums
