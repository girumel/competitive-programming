class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word in {word.upper(), word.lower(), word.title()}:
            return True
        else:
            return False