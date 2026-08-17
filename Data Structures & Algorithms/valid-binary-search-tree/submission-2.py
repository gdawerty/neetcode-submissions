# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def verify(root: Optional[TreeNode], left: float, right: float) -> bool:
            if not root:
                return True
            if not (left < root.val < right):
                return False

            return verify(root.left, left, root.val) and verify(root.right, root.val, right)



        return verify(root, float("-inf"), float("inf"))         