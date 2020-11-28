class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        m,n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        longest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    if j-1 >= 0 and i-1 >= 0:
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
                    else:
                        dp[i][j] = 1
                    if dp[i][j] > longest:
                        longest = dp[i][j]
        return longest*longest
            