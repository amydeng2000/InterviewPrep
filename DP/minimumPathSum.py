class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        i = len(grid)
        j = len(grid[0])
        mem = []
        for _ in range(i):
            mem.append([-1]*j)
        return self.helper(grid, i-1, j-1, mem)
        
    def helper(self, grid, i, j, mem):
        if i == 0 and j == 0: return grid[i][j]
        if i < 0 or j < 0: return float('inf')
        if mem[i][j] >= 0: return mem[i][j]
        mem[i][j] = grid[i][j] + min(self.helper(grid, i, j-1, mem), self.helper(grid, i-1, j, mem))
        return mem[i][j]
        