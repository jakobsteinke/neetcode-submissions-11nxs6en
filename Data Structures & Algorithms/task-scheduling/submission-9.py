class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ds for available tasks
        # after each cycle process ds for non av tasks
        # start with tasks with highest count
        # max heap for av tasks
        # queue for nv tasks, in queue: (name, count, timestamp)
        timestamp = 0
        av = [(-count, name) for name, count in Counter(tasks).items()]
        heapq.heapify(av)
        nav = deque()
        num_cycles = 0

        while av or nav:
            while nav and nav[0][2] == timestamp:
                name, count, _ = nav.popleft()
                heapq.heappush(av, (count, name))
            if av:
                count, name = heapq.heappop(av)
                count += 1
                if count < 0:
                    nav.append((name, count, timestamp + n + 1))
            
            num_cycles += 1
            timestamp += 1

        return num_cycles



