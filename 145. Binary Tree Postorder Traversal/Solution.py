# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._postorder(root, result)
        return result
    
    def _postorder(self, node: Optional[TreeNode], result: List[int]):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)