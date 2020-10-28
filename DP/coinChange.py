class Solution(object):
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