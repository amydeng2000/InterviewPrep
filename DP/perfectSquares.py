class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [-1]*(n+1)
        mem[0] = 0
        return self.helper(n, mem)
        
        
    def helper(self, n, mem):
        if mem[n] >= 0: return mem[n]
        minimum = float('inf')
        i = 1
        while i*i <= n:
            minimum = min(minimum, 1 + self.helper(n-i*i, mem))
            i += 1
        mem[n] = minimum
        return minimum