class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for n in range(num):
            digit_sum = 0
            while n != 0:
                digit_sum = n % 10
                n = n // 10
            if digit_sum % 2 == 0:
                count += 1
        return count