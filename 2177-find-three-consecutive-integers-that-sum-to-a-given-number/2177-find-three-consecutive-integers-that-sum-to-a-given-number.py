class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ints = []
        n = num // 3
        if (n - 1) + n + (n + 1) == num:
            ints.append(n - 1)
            ints.append(n)
            ints.append(n + 1)
        return ints
