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
        for i in range(0,amount+1):
            mem[i] = self.helper(coins, i, mem)
            print("mem[{0}] = {1}".format(i, mem[i]))
        if mem[amount] == float('inf'):
            return -1
        return mem[amount]
    
    def helper(self, coins, amount, mem):
        if amount == 0: return 0
        if amount < 0: return float('inf')
        if mem[amount] == float('inf'):
            for coin in coins:
                mem[amount] = min(mem[amount], 1+self.helper(coins, amount-coin, mem))
        return mem[amount]
        
    
s = Solution()
print(s.coinChange([1,2,5], 11))

        
        