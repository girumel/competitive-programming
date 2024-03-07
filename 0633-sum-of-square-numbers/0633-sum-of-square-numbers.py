class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 2:
            return True

        right = int(c**(1/2))
        for left in range(right+1):
            square_sum = left**2 + right**2
            if square_sum == c:
                return True
            elif square_sum < c:
                continue
            else:
                right -= 1

        return False