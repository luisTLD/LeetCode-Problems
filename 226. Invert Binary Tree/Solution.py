# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._invertTree(root)
        return root

    def _invertTree(self, node: Optional[TreeNode]):
        if node:
            tmp = node.left
            node.left = node.right
            node.right = tmp
            self._invertTree(node.left)
            self._invertTree(node.right)
