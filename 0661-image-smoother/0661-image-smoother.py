class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        smoothened = [[0 for r in range(cols)] for r in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                total = 0
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if r + i >= 0 and r + i < rows and c + j >= 0 and c + j < cols:
                            total += img[r+i][c+j]
                            count += 1
                smoothened[r][c] = total // count
        
        
        return smoothened
        