# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #compare boundaries of left and right child nodes
        #perform a dfs on left and right, compare values and ensure left < node < right


        def dfs(left, right, node) -> bool:
            if not node:
                return True

            if not left < node.val < right:
                return False

            return dfs(left, node.val, node.left) and dfs(node.val, right, node.right)



        
        return dfs(float('-inf'), float('inf'), root)