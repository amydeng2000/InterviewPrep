class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def complete(i):
            tank = 0
            for i in range(i, len(gas)):
                tank = tank + gas[i] - cost[i]
                if tank + gas[i] - cost[i] < 0: 
                    return False
            for i in range(i):
                tank = tank + gas[i] - cost[i]
                if tank + gas[i] - cost[i] < 0: 
                    return False
            return True
        for i in range(len(gas)):
            if complete(i): 
                return i
        return -1

s = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
s.canCompleteCircuit(gas,cost)