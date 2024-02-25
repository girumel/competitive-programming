class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before_pivot = [n for n in nums if n < pivot]
        after_pivot = [n for n in nums if n > pivot]
        
        return before_pivot + [pivot]*nums.count(pivot) + after_pivot