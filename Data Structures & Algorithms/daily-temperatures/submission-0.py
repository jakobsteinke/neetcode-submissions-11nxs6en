class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack of (temp, i)
        # stack with decreasing temperatures
        # 8 7 6 
        n = len(temperatures)
        res = [0] * n

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temp, i))

        return res
