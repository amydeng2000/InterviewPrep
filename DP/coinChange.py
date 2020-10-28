class SolutionIterative(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        if amount < 0: return -1
        mem = [float('inf')]*(amount+1)
        mem[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                mem[i] = min(mem[i], 1+mem[i-coin])
        if mem[amount] == float('inf'): return -1
        return mem[amount]


class SolutionRecursive(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mem = [float('inf')]*(amount+1)
        return self.helper(coins, amount, mem)
        
    def helper(self, coins, amount, mem):
        if amount == 0: return 0
        if amount < 0: return -1
        if mem[amount] != float('inf'): return mem[amount]
        minimum = float('inf')
        for coin in coins:
            flag = self.helper(coins, amount-coin, mem)
            if flag >= 0 and flag < minimum:
                minimum = 1+flag
        mem[amount] = -1 if minimum == float('inf') else minimum     
        return mem[amount]