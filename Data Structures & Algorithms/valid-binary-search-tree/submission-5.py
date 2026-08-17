# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def verify(node: Optional[TreeNode], left: float, right: float) -> bool:
            if node is None:
                return True
            
            elif left < node.val and right > node.val:
                return verify(node.left, left, node.val) and verify(node.right, node.val, right)

            else:
                return False
        
        return verify(root, float("-inf"), float("inf"))
