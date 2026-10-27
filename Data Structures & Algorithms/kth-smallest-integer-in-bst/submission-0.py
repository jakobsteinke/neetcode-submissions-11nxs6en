# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order_count = 1
        result = -1
    
        def dfs(node):
            nonlocal order_count
            nonlocal result
            if not node:
                return
            dfs(node.left)
            if order_count == k:
                result = node.val
            order_count += 1
            dfs(node.right)
        
        dfs(root)
        
        return result
        