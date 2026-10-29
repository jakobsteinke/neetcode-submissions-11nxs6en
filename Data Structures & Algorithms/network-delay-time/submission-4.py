class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = set()
        heap = [(0, k)]
        costs = [math.inf] * (n + 1)
        costs[k] = 0

        def relax(n1, n2, w):
            if costs[n1] + w < costs[n2]:
                costs[n2] = costs[n1] + w
                heapq.heappush(heap, (costs[n2], n2))

        while heap:
            cost, node = heapq.heappop(heap)
            if cost > costs[node]:
                continue
            visited.add(node)
            for nei, w in adj[node]:
                if nei not in visited:
                    relax(node, nei, w)
        
        if len(visited) != n:
            return -1
        return max(costs[1:])
