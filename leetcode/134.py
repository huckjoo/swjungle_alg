from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # 여기서부턴 무조건 답이 존재
        start = 0 
        fuel = 0
        for i in range(len(gas)):
            # 답이 안되는 경우
            if gas[i]+fuel < cost[i]:
                start = i+1
                fuel = 0
            else:
                fuel += gas[i]-cost[i]
        return start