class Solution:
    def compressedString(self, word: str) -> str:
        output = ""
        length = len(word)

        count = 0
        c = word[0]
        for i in range(length):
            if word[i] == c:
                if count == 9:
                    output += str(count) + c
                    count = 1
                else:
                    count += 1   
            else:
                output += str(count) + c
                c = word[i]
                count = 1
        output += str(count) + c

        return output
