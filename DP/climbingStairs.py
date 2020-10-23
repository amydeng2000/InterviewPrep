class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [-1]*(n+1)
        return self.helper(n, mem)
        
    def helper(self, n, mem):
        if n == 0:
            return 1
        if n < 0: 
            return 0
        if mem[n] < 0:
            mem[n] = self.helper(n-1, mem) + self.helper(n-2, mem)
        return mem[n]