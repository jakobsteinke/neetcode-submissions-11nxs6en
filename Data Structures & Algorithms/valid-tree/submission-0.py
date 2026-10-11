class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neis = defaultdict(list)
        for n1, n2 in edges:
            neis[n1].append(n2)
            neis[n2].append(n1)
        # check cycle
        queue = deque([(0,  -1)])
        seen = set([0])
        while queue:
            cur, last_node = queue.popleft()
            for nei in neis[cur]:
                if nei != last_node and nei in seen:
                    return False
                if nei != last_node:
                    queue.append((nei, cur))
                    seen.add(nei)
        if len(seen) != n:
            return False
        return True
