"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map = {}
        if not node:
            return None

        def dfs(node):
            copyNode = Node(node.val, [])
            map[node.val] = copyNode
            for nei in node.neighbors:
                if nei.val not in map:
                    dfs(nei)
                copyNode.neighbors.append(map[nei.val])
            
        dfs(node)
        return map[node.val]