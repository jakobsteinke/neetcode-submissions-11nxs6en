# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def verify(node, left_boundary, right_boundary):
            if not node:
                return True
            if node.val <= left_boundary or node.val >= right_boundary:
                return False
            return (verify(node.left, left_boundary, min(right_boundary, node.val)) and
            verify(node.right, max(left_boundary, node.val), right_boundary))

        return verify(root, -math.inf, math.inf)
      

            
