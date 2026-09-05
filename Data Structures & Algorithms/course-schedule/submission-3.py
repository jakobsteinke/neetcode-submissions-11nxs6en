class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for second, first in prerequisites:
            adj[first].append(second)

        def dfs(course, visited):
            if course in visited:
                return False
            if course in finished:
                return True
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei, visited):
                    return False
            finished.add(course)
            visited.remove(course) 
            return True
        
        finished = set()
        
        for course in range(numCourses):
            if course not in finished:
                if not dfs(course, set()):
                    return False

        return True