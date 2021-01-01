class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # wordBreak(i): for j < i: wordBreak(j) and s[j:i] in wordDict
        # memo saves whether up to ith index, s can be broken down
        
        memo = [None]* len(s)
        def helper(i):
            if i == -1: return True
            if memo[i] != None: return memo[i]
            for j in range(-1, i):
                if helper(j) and s[j+1:i+1] in wordDict: 
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return helper(len(s)-1)