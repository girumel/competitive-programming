class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        del_columns = 0
        
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j - 1][i]:
                    del_columns += 1
                    break
        
        return del_columns
                