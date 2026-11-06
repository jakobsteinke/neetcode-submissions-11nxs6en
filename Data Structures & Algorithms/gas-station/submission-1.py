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
            if cur_gas - cur_cost < 0:
                result_idx = i + 1
                cur_gas = 0
                cur_cost = 0
        return result_idx