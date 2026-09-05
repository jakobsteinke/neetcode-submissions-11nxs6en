class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numComp = 0
        finished = set()
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def bfs(node):
            finished.add(node)
            queue = deque([node])
            while queue:
                cur = queue.popleft()
                finished.add(cur)
                for nei in graph[cur]:
                    if nei not in finished:
                        queue.append(nei)

        for node in range(n):
            if node not in finished:
                numComp += 1
                bfs(node)

        return numComp