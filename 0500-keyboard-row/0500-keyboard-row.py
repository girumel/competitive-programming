class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        thrid_row = set("zxcvbnm")
        one_row_words = []
        for word in words:
            letters = set(word.lower())
            if letters <= first_row or letters <= second_row or letters <= thrid_row:
                one_row_words.append(word)
        return one_row_words
                