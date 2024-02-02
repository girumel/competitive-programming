class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            j = 1
            c = strs[0][i]
            while j < len(strs):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
                j += 1
            i += 1
        return strs[0]
