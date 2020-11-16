class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [-1]*(n+1)
        mem[0] = 0
        return self.helper(n, mem, 0)
        
    def helper(self, n, mem, split):
        if mem[n] > 0: return mem[n]
        if split == 0: m = -1
        else: m = n
        for i in range(1, n+1):
            m = max(i*self.helper(n-i, mem, split+1), m)
        mem[n] = m
        return mem[n]