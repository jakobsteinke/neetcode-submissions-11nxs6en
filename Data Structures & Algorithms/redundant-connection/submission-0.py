class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for n1, n2 in edges:
            n = max(n, n1, n2)
        leader = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def find(node):
            if leader[node] == node:
                return node
            leader[node] = find(leader[node])
            return leader[node]

        def union(n1, n2):
            l1, l2 = find(n1), find(n2)
            if l1 == l2:
                return False
            if size[l1] > size[l2]:
                leader[l2] = l1
                size[l1] += size[l2]
            else:
                leader[l1] = l2
                size[l2] += size[l1]
            return True

        for edge in edges:
            n1, n2 = edge
            if not union(n1, n2):
                return edge
        
        return []