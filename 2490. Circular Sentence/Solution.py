class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        length = len(sentence)
        if sentence[0] != sentence[length - 1]:
            return False
        for i in range(length):
            if sentence[i] == ' ':
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return True