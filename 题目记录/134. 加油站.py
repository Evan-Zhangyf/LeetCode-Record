class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        while cur < len(gas):
            gas_sum = 0
            for i in range(len(gas)):
                gas_sum += gas[(cur+i)%len(gas)] - cost[(cur+i)%len(gas)]
                if gas_sum < 0:
                    cur = cur + i + 1
                    break
                if i == len(gas) - 1 and gas_sum >= 0:
                    return cur
        return -1