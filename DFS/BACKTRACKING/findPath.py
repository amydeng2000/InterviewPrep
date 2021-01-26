matrix = [
    [1,1,1],
    [0,1,0],
    [0,1,1]

]

def findPath(matrix):
    M = len(matrix)
    N = len(matrix[0])
    dp = [[0 for _ in range(N)] for _ in range(M)]
    res = []
    steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def dfs(i,j):
        if i == M-1 and j == N-1:
            res.append((i,j))
            return True
        if i < 0 or i >= M or j < 0 or j >= N or matrix[i][j] == 0 or dp[i][j] == 1:
            return False
        if dp[i][j] == -1:
            return False
        res.append((i, j))
        dp[i][j] = 1
        for m,n in steps:
            x = i+m
            y = j+n
            if dfs(x,y) == True:
                return True
        dp[i][j] = -1
        res.pop()
        return dp[i][j]
    
    dfs(0,0)
    return res

print(findPath(matrix))