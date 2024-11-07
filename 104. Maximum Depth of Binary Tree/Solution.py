# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        num = [1]
        self.foo(root, num, 1)
        return num[0]   

    def foo(self, node: Optional[TreeNode], num: List[int], depth: int):
        if node:
            self.foo(node.left, num, depth + 1)
            self.foo(node.right, num, depth + 1)
            if depth > num[0]:
                num[0] = depth