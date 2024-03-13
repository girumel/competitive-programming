class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []

        for i in range(len(arr), 1, -1):
            index = arr.index(i)
            if index != i - 1:
                arr[:index + 1] = arr[:index + 1][::-1]
                arr[:i] = arr[:i][::-1]

                flips.append(index + 1)
                flips.append(i)

        return flips