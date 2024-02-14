class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(n) for n in list(str(int(''.join([str(digit) for digit in digits])) + 1))]
        