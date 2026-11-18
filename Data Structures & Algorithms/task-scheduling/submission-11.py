class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        av = [(-count, name) for name, count in Counter(tasks).items()]
        heapq.heapify(av)
        nav = deque()
        num_cycles = 0

        while av or nav:
            while nav and nav[0][2] == num_cycles:
                name, count, _ = nav.popleft()
                heapq.heappush(av, (count, name))
            if av:
                count, name = heapq.heappop(av)
                count += 1
                if count < 0:
                    nav.append((name, count, num_cycles + n + 1))
            
            num_cycles += 1
        return num_cycles



