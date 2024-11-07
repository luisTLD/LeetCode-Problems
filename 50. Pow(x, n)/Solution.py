class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        is_negative = n < 0
        n = abs(n)
        
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return 1 / result if is_negative else result
