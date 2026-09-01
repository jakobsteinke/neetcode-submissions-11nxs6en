class MinStack:

    def __init__(self):
        # each value on stack carries index of min before that element was pushed, when popping this, we reset the index
        self.minIndex = 0
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, self.minIndex))
        if val < self.stack[self.minIndex][0]:
            self.minIndex = len(self.stack) - 1

    def pop(self) -> None:
        _, pastMinIndex = self.stack.pop()
        self.minIndex = pastMinIndex
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[self.minIndex][0]
