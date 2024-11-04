class Solution:
    def compressedString(self, word: str) -> str:
        output = ""
        length = len(word)

        count = 1
        c = word[0]
        for i in range(1, length):
            if word[i] == c and count < 9:
                count += 1   
            else:
                output += str(count) + c
                c = word[i]
                count = 1
        output += str(count) + c

        return output
