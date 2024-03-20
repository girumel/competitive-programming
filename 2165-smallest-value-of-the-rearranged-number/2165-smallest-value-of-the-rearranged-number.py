class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        elif num < 0:
            num = -1 * num
            digits = [int(d) for d in str(num)]
            digits.sort(reverse=True)
            return -int(''.join(map(str, digits)))
        else:
            digits = [int(d) for d in str(num)]
            digits.sort()
            if digits[0] == 0:
                for i in range(1, len(digits)):
                    if digits[i] != 0:
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int(''.join(map(str, digits)))
            