class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        dproduct = 1
        dsum = 0
        while n != 0:
            dsum += n % 10
            dproduct *= n % 10
            n = n // 10
        return dproduct - dsum
            