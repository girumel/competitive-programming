class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        for i in range(size):
            max_index = i
            for j in range(i + 1, size):
                if heights[max_index] < heights[j]:
                    max_index = j
            heights[i], heights[max_index] = heights[max_index], heights[i]
            names[i], names[max_index] = names[max_index], names[i]
        return names
