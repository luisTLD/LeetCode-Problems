# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.foo(nums, 0, len(nums) - 1)

    def foo(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.foo(nums, left, mid - 1)
        root.right = self.foo(nums, mid + 1, right)

        return root