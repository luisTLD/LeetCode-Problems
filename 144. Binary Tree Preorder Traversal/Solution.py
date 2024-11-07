# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder(root, result)
        
        return result
    
    def _preorder(self, node: Optional[TreeNode], result: List[int]):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)