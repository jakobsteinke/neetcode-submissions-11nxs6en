# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 1, 2, ... 3, 4 ,5 
        # preorder with nones, return when 2x none, return next index
        # # -> separation, % -> None
        l = []
        def dfs(node):
            if not node:
                l.append('%')
                return
            l.append(str(node.val) + '#')
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "".join(l)
           
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        def dfs(index):
            # assume idx in bounds
            if data[index] == '%':
                return (index + 1, None)
            else:
                node = TreeNode()
                num = 0
                isNeg = False
                if data[index] == '-':
                    isNeg = True
                    index += 1
                while data[index] != '#':
                    num = num * 10 + int(data[index])
                    index += 1
                if isNeg:
                    num = -num
                node.val = num
                index += 1

                index, node.left = dfs(index)
                if index < len(data):
                    index, node.right = dfs(index)
                return (index, node)    

        return dfs(0)[1]













