# Given an mxn grid of 0s,1s and 2s (0 denoting an obstacle, 1 denoting empty cell and 2 denoting cell with gold). 
# Find the path used to reach from (0,0) to (m - 1, n - 1) collecting maximum gold if you are allowed to travel 
# in any four directions and can take a maximum of k steps.

def mining(grid, k):
    visited = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
    maxPath = {}
    
    def dfs(i, j, curr, path):
        if k < 0: return -float('inf')
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]): return -float('inf')
        if grid[i][j] == 0 or visited[i][j] > 0: return -float('inf')
        gold = (1 if grid[i][j] == 2 else 0)
        path.append((i,j))
        if i == len(grid)-1 and j == len(grid[i])-1: 
            maxPath[curr+gold] = path
            return curr+gold
        visited[i][j] = 1
        maximum = - float('inf')
        maximum = max(maximum, dfs(i+1, j, curr+gold, path[:]))
        maximum = max(maximum, dfs(i-1, j, curr+gold, path[:]))
        maximum = max(maximum, dfs(i, j+1, curr+gold, path[:]))
        maximum = max(maximum, dfs(i, j-1, curr+gold, path[:]))
        visited[i][j] = -1
        return maximum
    

    gold = dfs(0, 0, 0, [])
    return(maxPath[gold])







grid = [[1,2,0], [1,1,0], [1,1,1]]
print(mining(grid, 10))