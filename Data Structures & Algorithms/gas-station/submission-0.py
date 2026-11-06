class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # look at cost needed 
        if sum(cost) > sum(gas):
            return -1
        result_idx = 0
        cur_gas = cur_cost = 0
        for i in range(len(gas)):
            cur_gas += gas[i]
            cur_cost += cost[i]
            while cur_gas - cur_cost < 0:
                cur_gas -= gas[result_idx]
                cur_cost -= cost[result_idx]
                result_idx += 1
        return result_idx