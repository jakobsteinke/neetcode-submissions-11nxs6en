# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if not root:
                return 0
            chr = getHeight(root.right)
            chl = getHeight(root.left)
            if chr == -1 or chl == -1 or abs(chr - chl) > 1:
                return -1
            return max(chr, chl) + 1
        
        return getHeight(root) != -1