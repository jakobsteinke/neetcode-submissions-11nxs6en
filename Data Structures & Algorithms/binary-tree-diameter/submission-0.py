# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxD = 0
    def traverseTree(self, root):
        if not root:
            return 0
        leftD = self.traverseTree(root.left)
        rightD = self.traverseTree(root.right)
        self.maxD = max(self.maxD, leftD + rightD)
        return 1 + max(leftD, rightD)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverseTree(root)
        return self.maxD