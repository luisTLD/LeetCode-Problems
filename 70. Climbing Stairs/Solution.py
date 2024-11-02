class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        array = [0] * n
        array[0] = 1
        array[1] = 2
        for i in range(2, n):
            array[i] = array[i - 1] + array[i - 2]

        return array[n - 1]