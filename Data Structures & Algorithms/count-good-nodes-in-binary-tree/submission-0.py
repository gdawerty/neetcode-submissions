# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxSoFar):
            if not node:
                return 0

            good = 1 if node.val >= maxSoFar else 0

            maxNow = max(maxSoFar, node.val)

            left_good = dfs(node.left, maxNow)
            right_good = dfs(node.right, maxNow)

            return good + left_good + right_good
        
        if not root:
            return 0

        # start from root: maxSoFar is root.val initially
        return dfs(root, root.val)