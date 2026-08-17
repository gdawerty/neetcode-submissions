# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def helper(root: Optional[TreeNode], nodes: list) -> None:
            if not root:
                return

            helper(root.left, nodes)
            nodes.append(root.val)
            helper(root.right, nodes)

        nodes = []

        helper(root, nodes)

        return nodes[k-1]
