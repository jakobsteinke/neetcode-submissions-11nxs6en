class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        metaData = [(position[i], speed[i]) for i in range(len(position))]
        metaData.sort(key=lambda x: x[0])
        stack = []
        for i in range(len(position)):
            positionI, speedI = metaData[i]
            stack.append((target - positionI) / speedI)
        fleetCounter = 0
        while stack:
            time = stack.pop()
            fleetCounter += 1
            while stack and stack[-1] <= time:
                stack.pop()
        return fleetCounter

        # 4107    6 9 10 3   3 5 10 3

        # 3 3 5 10


