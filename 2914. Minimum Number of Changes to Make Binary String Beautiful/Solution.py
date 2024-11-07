class Solution:
    def minChanges(self, s: str) -> int:
        y = len(s)
        x = 0
        
        for i in range(1, y, 2):
            if s[i] != s[i - 1]:
                x += 1

        return x