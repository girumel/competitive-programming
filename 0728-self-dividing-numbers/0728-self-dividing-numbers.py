class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right + 1):
            org = i
            divs = []
            if str(i).find('0') != -1:
                continue

            while i != 0:
                divs.append(i % 10)
                i //= 10

            if all([org % div == 0 for div in divs]):
                nums.append(org)
        return nums
        