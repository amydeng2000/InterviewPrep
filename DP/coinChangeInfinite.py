class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        mem = {}
        return self.helper(amount, coins, 0, mem)
        
    def helper(self, amount, coins, i, mem):
        if amount == 0: return 1
        if amount < 0 or i >= len(coins): return 0
        if (amount, i) in mem: return mem[(amount, i)]
        m = 0
        for j in range(amount//coins[i] +1):
            m += self.helper(amount-j*coins[i], coins, i+1, mem)
        mem[(amount, i)] = m
        return mem[(amount, i)]