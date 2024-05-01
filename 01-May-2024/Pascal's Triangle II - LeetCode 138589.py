# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex+1)

        for i in range(rowIndex+1):
            for j in range(i-1, 0, -1):
                row[j] += row[j-1]
        
        return row