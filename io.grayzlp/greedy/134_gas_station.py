"""
https://leetcode.com/problems/gas-station/description/

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        tank = 0
        costs = 0
        gass = 0
        for i in range(0, len(gas)):
            costs += cost[i]
            gass += gas[i]
            if tank + gas[i] < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]
        if costs > gass:
            return -1
        else:
            return start


# Test code
print Solution().canCompleteCircuit([0, 0, 0, 10], [3, 2, 1, 4])
