# Problem: Maximize the Confusion of an Exam - https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        question = {'T': 0, 'F': 0}
        max_count = 0
        left, right = 0, 0
            
        while right < n:
            question[answerKey[right]] += 1
            right += 1

            while min(question['T'], question['F']) > k:
                question[answerKey[left]] -= 1
                left += 1

            max_count = max(max_count, right - left)

        return max_count