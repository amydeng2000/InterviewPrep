class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0: return 0
        mem = []
        for _ in range(m):
            mem.append([-1]*n)
        mem[m-1][n-1] = 1
        return self.helper(mem, 0, 0)
        
    def helper(self, mem, r, c):
        if r == len(mem)-1 and c == len(mem[0])-1: return mem[r][c]
        if r >= len(mem) or c >= len(mem[0]): return 0
        if mem[r][c] >= 0: return mem[r][c]
        mem[r][c] = self.helper(mem, r+1, c) + self.helper(mem, r, c+1)
        return mem[r][c]
        