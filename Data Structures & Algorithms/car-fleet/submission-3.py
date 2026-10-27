class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can caluclate how many steps each car needs: math.ceil((target - pos) / speed)
        # fleetleader
        # as long as cur car numsteps <= fleetleader, will be in the same fleet
        # once numsteps > fleetleader, new fleet where this car is the leader

        stack = []
        num_fleets = 0
        for p, s in sorted(zip(position, speed), key=lambda x:x[0]):
            stack.append((target - p) / s)
        fleet_leader = -math.inf
        while stack:
            cur = stack.pop()
            if cur > fleet_leader:
                num_fleets += 1
                fleet_leader = cur
        
        return num_fleets