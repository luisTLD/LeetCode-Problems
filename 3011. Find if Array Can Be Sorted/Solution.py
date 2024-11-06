class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        loop = len(nums)

        dic_big = {0: nums[0]}
        dic_small = {0: nums[0]}
        seg_nums = 0

        save = self.bitNum(nums[0])
        for i in range(1, loop):
                
            current = self.bitNum(nums[i])
            if current != save:
                save = current
                dic_big[i] = nums[i]
                seg_nums += 1
                dic_big[seg_nums] = nums[i]
                dic_small[seg_nums] = nums[i]
            else:
                if dic_big[seg_nums] < nums[i]:
                    dic_big[seg_nums] = nums[i]
                elif dic_small[seg_nums] > nums[i]:
                    dic_small[seg_nums] = nums[i]

        if seg_nums == 0:
            return True

        for i in range(seg_nums):
            if dic_big[i] > dic_small[i + 1]:
                return False

        return True

    def bitNum(self, num1: int) -> int:
        x = 0
        while num1 > 0:
            if num1 % 2 == 1:
                x += 1
            num1 //= 2

        return x