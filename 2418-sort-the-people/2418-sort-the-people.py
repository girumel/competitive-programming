class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        for i in range(1, size):
            h_key = heights[i]
            n_key = names[i]
            
            j = i - 1
            while j >= 0 and heights[j] < h_key:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1
            heights[j+1] = h_key
            names[j+1] = n_key
        
        return names
