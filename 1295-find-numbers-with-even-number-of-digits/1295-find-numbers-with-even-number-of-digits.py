class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_nums = list(map(str, nums))
        count = 0
        for str_num in str_nums:
            if len(str_num) % 2 == 0:
                count += 1
        return count
        