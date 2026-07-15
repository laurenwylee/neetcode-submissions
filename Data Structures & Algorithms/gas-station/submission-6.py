class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        min_idx = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                min_idx = i + 1
        return min_idx