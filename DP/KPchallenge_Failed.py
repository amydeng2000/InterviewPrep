def reachTheEnd(grid, maxTime):
    if len(grid) == 0: return 'Yes'
    memo = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
    steps = helper(grid, 0, 0, memo, maxTime)
    if steps <= maxTime: return 'Yes'
    return 'No'
    
def helper(grid, i, j, memo):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '#' or maxTime < 0:
        return float('inf')
    if i == len(grid)-1 and j == len(grid[i])-1: 
        return 0
    if memo[i][j] > 0: 
        return memo[i][j]
    steps = float('inf')
    memo[i][j] = float('inf')
    steps = min(steps, helper(grid, i+1, j, memo, maxTime-1))
    steps = min(steps, helper(grid, i-1, j, memo, maxTime-1))
    steps = min(steps, helper(grid, i, j+1, memo, maxTime-1))
    steps = min(steps, helper(grid, i, j-1, memo, maxTime-1))
    memo[i][j] = steps
    return memo[i][j]

print(reachTheEnd( ['..##', '#.##', '#...'], 5))