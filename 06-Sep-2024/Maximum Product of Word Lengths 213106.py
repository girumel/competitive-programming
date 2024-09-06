# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        max_product = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if not set(words[i]) & set(words[j]):
                    max_product = max(max_product, len(words[i])*len(words[j]))
        return max_product