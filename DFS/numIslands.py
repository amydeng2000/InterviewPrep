class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    count += self.dfs(grid, i, j, visited)
        return count
                    
    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]): return 0
        if visited[i][j]: return 0
        visited[i][j] = 1
        if grid[i][j] == "0": return 0
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i, j-1, visited)
        self.dfs(grid, i, j+1, visited)
        return 1
                    
                    
                    