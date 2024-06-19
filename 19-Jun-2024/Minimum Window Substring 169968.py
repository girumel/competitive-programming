# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        s_freq = {}
        left, right = 0, 0
        count = 0
        min_length = n + 1
        start = 0

        while right < n:
            s_freq[s[right]] = s_freq.get(s[right], 0) + 1
            if s[right] in t_freq and s_freq[s[right]] <= t_freq[s[right]]:
                count += 1
            while count == m:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left
                s_freq[s[left]] -= 1
                if s[left] in t_freq and s_freq[s[left]] < t_freq[s[left]]:
                    count -= 1
                left += 1
            right += 1

        if min_length == n + 1:
            return ""
        else:
            return s[start:start + min_length]