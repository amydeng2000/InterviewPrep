# class Solution(object):
#     def integerBreak(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         mem = [-1]*(n+1)
#         mem[0] = 0
#         return self.helper(n, mem, 0)
        
#     def helper(self, n, mem, split):
#         if mem[n] > 0: return mem[n]
#         if split == 0: m = -1
#         else: m = n
#         for i in range(1, n+1):
#             m = max(i*self.helper(n-i, mem, split+1), m)
#         mem[n] = m
#         return mem[n]

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # prod = currInt * integerBreak(n-currInt)        
        # dp[i] = integerBreak(i)
        # helper function (n, prod) - recursive calls
        # base cases: n == 0: return prod; directly return dp stored value
        # go through all nums smaller than or equal to currNum, find max product, save to dp
        
        v# prod = currInt * integerBreak(n-currInt)        
        # dp[i] = integerBreak(i)
        # helper function (n, prod) - recursive calls
        # base cases: n == 0: return prod; directly return dp stored value
        # go through all nums smaller than or equal to currNum, find max product, save to dp
        
        dp = [-1 for _ in range(n+1)]
        def helper(n, split):
            if n == 0: return prod
            if dp[n] > 0: return dp[n]
            if split == 0: maxP = 0 
            else: maxP = n
            for i in range(1,n):
                maxP = max(maxP, i*helper(n-i, split+1))
            dp[n] = maxP
            return dp[n]
        
        return helper(n, 0)