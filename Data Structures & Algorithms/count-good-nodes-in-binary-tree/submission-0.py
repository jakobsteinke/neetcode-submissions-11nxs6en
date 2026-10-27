# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of max on path

        def dfs(node, max_val_so_far):
            num_good_nodes = 0
            if not node:
                return 0
            if max_val_so_far <= node.val:
                num_good_nodes += 1
            max_val_so_far = max(max_val_so_far, node.val)
            num_good_nodes += (dfs(node.left, max_val_so_far) + dfs(node.right, max_val_so_far))
            return num_good_nodes

        return dfs(root, -math.inf)