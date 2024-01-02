class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        result = []
        for num in nums:
            if freq[num] >= len(result):
                result.append([])
                
            result[freq[num]].append(num)
            freq[num] += 1
        
        return result
