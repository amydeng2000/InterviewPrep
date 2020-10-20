class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # To cash it, we create an array and build it up from the bottom
        G = [0]*(n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2,n+1):  # i = index of G
            for j in range(i):
                G[i] += G[j]*G[i-1-j]
        return G[n]
        
        # THIS EXCEEDS TIME LIMIT BECAUSE WE DON'T CASH THE NUMTREES CALLS
        # if n == 0 or n == 1: return 1
        # total = 0
        # for i in range(n):
        #     total += self.numTrees(i) * self.numTrees(n-1-i)
        # return total