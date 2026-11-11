# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # p -> c -> r or p -> c -> l or l -> c -> r
        # return max p path to parent 
        # always consider non-p path as well 
        max_path = -math.inf

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            max_l_path = dfs(node.left)
            max_r_path = dfs(node.right)

            return_path = max(max_l_path, max_r_path) + node.val if max(max_l_path, max_r_path) > 0 else node.val
            max_path = max(max_path, return_path, max_l_path + node.val + max_r_path, max_l_path + node.val, max_r_path + node.val)

            return return_path

        dfs(root)
        return max_path
            


        