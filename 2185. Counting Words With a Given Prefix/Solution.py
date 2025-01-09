class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total = 0
        l = len(pref)

        for word in words:
            if len(word) >= l:

                match = True
                for i in range(l):
                    if word[i] != pref[i]:
                        match = False
                        break                
                if match:
                    total += 1

        return total