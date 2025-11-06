from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        total = len(t)
        min_size = len(s) + 1
        left = right = 0
        result = ""
        while right < len(s):
            if s[right] in freq_t:
                if freq_t[s[right]] > 0:
                    total -= 1
                freq_t[s[right]] -= 1
            while total == 0:
                if min_size > right - left + 1:
                    min_size = right - left + 1
                    result = s[left:right + 1]

                if s[left] in freq_t:
                    freq_t[s[left]] += 1
                    if freq_t[s[left]] > 0:
                        total += 1
                left += 1
            right += 1
        return result
