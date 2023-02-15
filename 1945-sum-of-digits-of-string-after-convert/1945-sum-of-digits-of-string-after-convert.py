class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ''
        for c in s:
            convert += str(ord(c) - 96)
        num = int(convert)
        while k != 0:
            digit_sum = 0
            while num != 0:
                digit_sum += num % 10
                num = num // 10
            k -= 1
            num = digit_sum
        return digit_sum
        