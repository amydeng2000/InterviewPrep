# class Solution(object):
#     def minPathSum(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         if len(grid) == 0: return 0
#         i = len(grid)
#         j = len(grid[0])
#         mem = []
#         for _ in range(i):
#             mem.append([-1]*j)
#         return self.helper(grid, i-1, j-1, mem)
        
#     def helper(self, grid, i, j, mem):
#         if i == 0 and j == 0: return grid[i][j]
#         if i < 0 or j < 0: return float('inf')
#         if mem[i][j] >= 0: return mem[i][j]
#         mem[i][j] = grid[i][j] + min(self.helper(grid, i, j-1, mem), self.helper(grid, i-1, j, mem))
#         return mem[i][j]

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        # check boundry
        # if visited (memo > 0), return 
        # visit right, down, store min value in memo
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n: return float('inf')
            if i == m-1 and j == n-1: return grid[i][j]
            if memo[i][j] > 0: return memo[i][j]
            memo[i][j] = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
            return memo[i][j]
        
        return dfs(0, 0)

# s = Solution()
# s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])

print([1,2,3][:0])