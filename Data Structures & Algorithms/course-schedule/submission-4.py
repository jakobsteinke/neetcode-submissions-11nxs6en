class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()

        for a, b in prerequisites:
            adj[b].append(a)

        def dfs(node, recursion_stack):
            visited.add(node)
            recursion_stack.add(node)
            res = True
            for neighbor in adj[node]:
                if neighbor in recursion_stack:
                    return False
                if neighbor in visited:
                    continue
                res = res and dfs(neighbor, recursion_stack)
            recursion_stack.remove(node)
            return res

        for node in range(numCourses):
            if node not in visited and not dfs(node, set()):
                return False

        return True

