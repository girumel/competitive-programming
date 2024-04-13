# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        vowel_strings = []
        prefix_sum = [0]

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                vowel_strings.append(1)
            else:
                vowel_strings.append(0)

        for vs in vowel_strings:
            prefix_sum.append(prefix_sum[-1] + vs)

        ans = []
        for li, ri in queries:
            ans.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return ans