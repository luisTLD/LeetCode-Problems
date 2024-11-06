class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        loop = len(nums)
        old_big = 0
        big = 0
        small = 0

        save = self.bitNum(nums[0])
        for i in range(loop):
            current = self.bitNum(nums[i])
            if save != current:
                if old_big > nums[small]:
                    return False

                old_big = nums[big]
                small = i
                big = i
                save = current
            else:
                if nums[big] < nums[i]:
                    big = i
                elif nums[small] > nums[i]:
                    small = i

        if old_big > nums[small]:
            return False

        return True

    def bitNum(self, num: int) -> int:
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count