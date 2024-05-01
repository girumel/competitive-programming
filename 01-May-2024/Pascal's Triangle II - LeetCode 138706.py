# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        previous_row = self.getRow(rowIndex - 1)
        row = [1]
        for i in range(1, rowIndex):
            row.append(previous_row[i-1] + previous_row[i])
        row.append(1)

        return row