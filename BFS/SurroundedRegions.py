class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # visit[i][j] = True, False
        # visited all O's on the boarder, BFS, mark the grids as .
        # turn . into O, turn O into X
        
        # BFS
        if not board: return board
        M = len(board)
        N = len(board[0])
        
        def isValid(i,j):
            return i >= 0 and i < M and j >= 0 and j < N and board[i][j] == "O"
        
        from collections import deque
        q = deque()
        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M-1 or j == 0 or j == N-1) and board[i][j] == "O":
                    q.append((i,j))
        while q:
            x,y = q.popleft()
            board[x][y] = "."
            for i,j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if isValid(i,j):
                    q.append((i,j))
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"
        return board

        
        # DFS
        if not board: return board
        M = len(board)
        N = len(board[0])
        
        def isValid(i,j):
            return i >= 0 and i < M and j >= 0 and j < N and board[i][j] == "O"
        
        def dfs(x, y):
            board[x][y] = "."
            for i,j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if isValid(i,j):
                    dfs(i,j)
        
        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M-1 or j == 0 or j == N-1) and board[i][j] == "O":
                    dfs(i,j)
                    
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"
        return board
        