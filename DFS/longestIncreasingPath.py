# Mistakes
# Iterating each grid anyways, so we don't need to do increasing and decreasing, just one
# don't need to pass in length of the path so far to the dfs function because what you care about is storing and returning the longest path forward from that point, nothing from the path it came from matters, except that you don't want to revisit cells
# where to add the current cell to maximum?
# what base case comes first?

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        memo = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        def dfs(i, j, visited, pi, pj):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]): return 0
            if visited[i][j]: return 0
            if pi >= 0 and pj >= 0:
                if not matrix[i][j] - matrix[pi][pj]>0: return 0
            if memo[i][j] > 0: return memo[i][j]
            visited[i][j] = True
            maximum = 0
            maximum = max(maximum, dfs(i+1,j,visited,i,j))
            maximum = max(maximum, dfs(i-1,j,visited,i,j))
            maximum = max(maximum, dfs(i,j+1,visited,i,j))
            maximum = max(maximum, dfs(i,j-1,visited,i,j))
            visited[i][j] = False
            memo[i][j] = maximum+1
            return memo[i][j]
        
        maximum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                maximum = max(maximum, dfs(i,j,visited,-1,-1))
        return maximum


s = Solution()
matrix = [[9,8,4],[6,6,8],[2,1,1]]
print(s.longestIncreasingPath(matrix))