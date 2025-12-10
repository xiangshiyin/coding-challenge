class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        ix = 0
        start = 0
        fuel = 0
        while ix < 2 * n:
            fuel += gas[ix % n]
            fuel -= cost[ix % n]
            if fuel < 0:
                start = (ix + 1) % n  # reset start point
                fuel = 0  # reset fuel
            else:
                if (ix + 1) % n == start:
                    return start
            ix += 1
        return -1
