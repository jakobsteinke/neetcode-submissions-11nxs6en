class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        global_solution = 0
        for uppercase_letter in uppercase_letters:
            local_solution = 0
            queue = deque()
            l = 0
            # TODO k = 0
            for r in range(len(s)):
                if s[r] != uppercase_letter:
                    if k == 0:
                        l = r + 1
                    else:
                        if len(queue) == k:
                            l = queue.popleft() + 1
                        queue.append(r)
                local_solution = max(local_solution, r - l + 1)
            global_solution = max(global_solution, local_solution)
        return global_solution
        
