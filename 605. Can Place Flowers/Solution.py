class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        end = len(flowerbed) - 1

        while n > 0 and i < end - 1:
            if flowerbed[i] == 0:
                if flowerbed[i + 1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 3
            else:
                i += 2
        
        if flowerbed[end - 1] == 0 and flowerbed[end] == 0:
            n -= 1

        return n <= 0