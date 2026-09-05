class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for second, first in prerequisites:
            adj[first].append(second)

        def dfs(course, visited, path):
            if course in visited:
                return []
            if course in finished:
                return [-1]
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei, visited, path):
                    return []
            finished.add(course)
            visited.remove(course) 
            path.append(course)
            return path
        
        finished = set()
        result = []
        for course in range(numCourses):
            if course not in finished:
                path = dfs(course, set(), [])
                if not path:
                    return []
                result.extend(path)
        
        result.reverse()
        return result