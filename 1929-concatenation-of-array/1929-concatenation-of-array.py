class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 2
        while count:
            for i in nums:
                ans.append(i)
            count -= 1
        return ans
            