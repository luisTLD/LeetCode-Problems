class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sum = {}
        length = len(nums)
        
        for index in range(length):
            complement = target - nums[index]
            if complement in hash_sum:
                return [hash_sum[complement], index]

            hash_sum[nums[index]] = index
        return []