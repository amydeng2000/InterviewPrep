class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        M = len(grid)
        N = len(grid[0])
        visited = [[False for j in range(N)] for i in range(M)]
        
        def dfs(i, j, area):
            visited[i][j] = True
            if grid[i][j] == 0: return area
            area += 1
            neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for r, c in neighbors:
                row = r + i
                col = c + j
                if row >= 0 and row < M and col >= 0 and col < N and not visited[row][col]:
                    area = dfs(row, col, area)
            return area 
        
        largest = 0
        for i in range(M):
            for j in range(N):
                if not visited[i][j]:
                    area = dfs(i, j, 0) 
                    largest = max(area, largest)
        return largest
            