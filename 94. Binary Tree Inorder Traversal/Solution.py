# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = [] 
        self.foo(root, values)
        
        return values

    def foo(self, node: Optional[TreeNode], values: List[int]):
        if node:
            self.foo(node.left, values)
            values.append(node.val)
            self.foo(node.right, values)