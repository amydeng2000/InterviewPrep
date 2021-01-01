class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        # dp[i][j] = longest common subsequence up to index i of text1, index j of text2
        # - N a b c d e
        # N 0 0 0 0 0 0
        # a 0 1 1 1 1 1
        # c 0 1 1 2 2 2 
        # e 0 1 1 2 2 3
        
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == 0 or j == 0: dp[i][j] = 0
                else: dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(dp[i][j-1], dp[i-1][j])
        return dp[len(text1)][len(text2)]
                