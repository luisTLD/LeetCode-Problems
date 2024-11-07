class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_combination = 0
        for bit in range(32):
            count = sum((num >> bit) & 1 for num in candidates)
            max_combination = max(max_combination, count)
        return max_combination
