# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def goDown(node, d):
            if not node:
                return d
            return max(goDown(node.left, d + 1), goDown(node.right, d + 1))
        return goDown(root, 0)